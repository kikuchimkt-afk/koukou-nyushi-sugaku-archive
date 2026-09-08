import { createHash } from "node:crypto";
import { copyFile, mkdir, readFile, readdir, rename, rm, stat, writeFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import path from "node:path";
import process from "node:process";

const args = parseArgs(process.argv.slice(2));
const repoRoot = path.resolve(import.meta.dirname, "..");
const sourceRoot = path.resolve(args["source-root"] || process.env.SOURCE_ROOT || "");
const pdftoppm = args.pdftoppm || process.env.PDFTOPPM || "pdftoppm";
const releaseTag = args["release-tag"] || process.env.RELEASE_TAG || "pdfs-v1";
const githubRepo = args["github-repo"] || process.env.GITHUB_REPO || "kikuchimkt-afk/koukou-nyushi-sugaku-archive";
const previewRoot = path.join(repoRoot, "public", "previews");
const releaseRoot = path.join(repoRoot, ".release-assets");
const dataPath = path.join(repoRoot, "data", "archive.generated.json");

if (!sourceRoot || sourceRoot === path.parse(sourceRoot).root) {
  fail("--source-root には既存のPDF最終版フォルダを含むディレクトリを指定してください。");
}

await assertDirectory(sourceRoot);
await mkdir(previewRoot, { recursive: true });
await mkdir(releaseRoot, { recursive: true });

const sourceDirs = await findFinalDirectories(sourceRoot);
if (!sourceDirs.length) fail(`最終版フォルダが見つかりません: ${sourceRoot}`);

const sourcePdfs = [];
for (const sourceDir of sourceDirs) {
  const names = await readdir(sourceDir);
  for (const name of names.filter((value) => value.toLowerCase().endsWith(".pdf"))) {
    sourcePdfs.push({ sourceDir, sourcePath: path.join(sourceDir, name), name });
  }
}

sourcePdfs.sort((a, b) => a.name.localeCompare(b.name, "ja"));
if (!sourcePdfs.length) fail("対象PDFがありません。");

const seenIds = new Set();
const items = [];

for (const [index, source] of sourcePdfs.entries()) {
  const parsed = parsePdfName(source.name);
  if (!parsed) {
    console.warn(`skip: ファイル名を解析できません: ${source.name}`);
    continue;
  }

  const field = detectField(source.sourceDir, parsed.unit);
  const id = makeId(parsed, field);
  if (seenIds.has(id)) fail(`重複ID: ${id}`);
  seenIds.add(id);

  const previewDir = path.join(previewRoot, id);
  await rm(previewDir, { recursive: true, force: true });
  await mkdir(previewDir, { recursive: true });

  const tempPrefix = path.join(previewDir, "render");
  const render = spawnSync(
    pdftoppm,
    [
      "-jpeg",
      "-scale-to-x",
      "1200",
      "-scale-to-y",
      "-1",
      "-jpegopt",
      "quality=76,optimize=y,progressive=y",
      source.sourcePath,
      tempPrefix,
    ],
    { encoding: "utf8", windowsHide: true },
  );
  if (render.status !== 0) {
    fail(`画像変換に失敗: ${source.name}\n${render.stderr || render.stdout}`);
  }

  const rendered = (await readdir(previewDir))
    .filter((name) => /^render-\d+\.jpg$/i.test(name))
    .sort((a, b) => pageNumber(a) - pageNumber(b));
  if (!rendered.length) fail(`プレビュー画像が生成されませんでした: ${source.name}`);

  const releaseName = `${id}.pdf`;
  const releasePath = path.join(releaseRoot, releaseName);
  await copyFile(source.sourcePath, releasePath);
  const contentVersion = createHash("sha256").update(await readFile(releasePath)).digest("hex");

  const previewPages = [];
  for (const [pageIndex, renderedName] of rendered.entries()) {
    const pageName = `page-${String(pageIndex + 1).padStart(2, "0")}.jpg`;
    await rename(path.join(previewDir, renderedName), path.join(previewDir, pageName));
    previewPages.push(`/previews/${id}/${pageName}?v=${contentVersion}`);
  }

  const fileStats = await stat(source.sourcePath);
  const { shortUnit, tags } = splitUnit(parsed.unit);

  items.push({
    id,
    grade: parsed.grade,
    year: parsed.year,
    prefecture: parsed.prefecture,
    field,
    unit: parsed.unit,
    shortUnit,
    tags,
    pageCount: previewPages.length,
    previewPages,
    contentVersion,
    pdfUrl: `https://github.com/${githubRepo}/releases/download/${releaseTag}/${releaseName}?rev=${contentVersion}`,
    pdfFileName: source.name,
    fileSize: fileStats.size,
  });

  console.log(`[${index + 1}/${sourcePdfs.length}] ${id} ${rendered.length}p ${source.name}`);
}

const wantedPreviewIds = new Set(items.map((item) => item.id));
for (const entry of await readdir(previewRoot, { withFileTypes: true })) {
  if (entry.isDirectory() && /^g[123]-/.test(entry.name) && !wantedPreviewIds.has(entry.name)) {
    await rm(path.join(previewRoot, entry.name), { recursive: true, force: true });
  }
}

const wantedReleaseNames = new Set(items.map((item) => `${item.id}.pdf`));
for (const entry of await readdir(releaseRoot, { withFileTypes: true })) {
  if (entry.isFile() && /^g[123]-.+\.pdf$/i.test(entry.name) && !wantedReleaseNames.has(entry.name)) {
    await rm(path.join(releaseRoot, entry.name), { force: true });
  }
}

items.sort((a, b) =>
  b.year - a.year ||
  a.field.localeCompare(b.field, "ja") ||
  a.prefecture.localeCompare(b.prefecture, "ja") ||
  a.unit.localeCompare(b.unit, "ja"),
);

const archive = {
  generatedAt: new Date().toISOString(),
  releaseTag,
  totalItems: items.length,
  totalPages: items.reduce((sum, item) => sum + item.pageCount, 0),
  items,
};

await writeFile(dataPath, `${JSON.stringify(archive, null, 2)}\n`, "utf8");
console.log(`完了: ${archive.totalItems}題 / ${archive.totalPages}ページ`);

function parseArgs(argv) {
  const result = {};
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i];
    if (!value.startsWith("--")) continue;
    result[value.slice(2)] = argv[i + 1];
    i += 1;
  }
  return result;
}

async function assertDirectory(target) {
  try {
    const info = await stat(target);
    if (!info.isDirectory()) throw new Error("not directory");
  } catch {
    fail(`source-root が存在しません: ${target}`);
  }
}

async function findFinalDirectories(root) {
  const entries = await readdir(root, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isDirectory() && /^中[123]数学_.+_最終版$/.test(entry.name))
    .map((entry) => path.join(root, entry.name));
}

function parsePdfName(filename) {
  const match = filename.match(/^(\d{4})年実施_(.+?)_(中([123]))数学_(.+)\.pdf$/);
  if (!match) return null;
  return {
    year: Number(match[1]),
    prefecture: match[2],
    grade: Number(match[4]),
    unit: match[5],
  };
}

function detectField(sourceDir, unit) {
  const parent = path.basename(sourceDir);
  if (parent.includes("_数と式_")) return "数と式";
  if (parent.includes("_図形_")) return "図形";
  if (parent.includes("_関数_")) return "関数";
  if (parent.includes("_データの活用_")) return "データの活用";
  return detectFieldFromUnit(unit);
}

// 領域は中学校学習指導要領の4領域（数と式・図形・関数・データの活用）に合わせる。
function detectFieldFromUnit(unit) {
  if (/度数|代表値|中央値|平均値|最頻値|相対度数|階級|ヒストグラム|箱ひげ|四分位|散らばり|確率|場合の数|標本|データ/.test(unit)) {
    return "データの活用";
  }
  if (/比例|反比例|一次関数|変化の割合|変域|グラフ|座標|関数/.test(unit)) return "関数";
  if (/図形|作図|角度|合同|証明|相似|円|三角形|四角形|多角形|平行|面積|体積|表面積|おうぎ形|立体|投影図|展開図|移動|ねじれ|柱|錐|球|線分/.test(unit)) {
    return "図形";
  }
  return "数と式";
}

function makeId(parsed, field) {
  const pref = prefectureCode(parsed.prefecture);
  const fieldCode = { 数と式: "algebra", 図形: "geometry", 関数: "function", データの活用: "data" }[field];
  const hash = createHash("sha1").update(parsed.unit).digest("hex").slice(0, 7);
  return `g${parsed.grade}-${parsed.year}-${pref}-${fieldCode}-${hash}`;
}

function prefectureCode(name) {
  const map = {
    北海道: "hokkaido", 青森県: "aomori", 岩手県: "iwate", 宮城県: "miyagi", 秋田県: "akita", 山形県: "yamagata", 福島県: "fukushima",
    茨城県: "ibaraki", 栃木県: "tochigi", 群馬県: "gunma", 埼玉県: "saitama", 千葉県: "chiba", 東京都: "tokyo", 神奈川県: "kanagawa",
    新潟県: "niigata", 富山県: "toyama", 石川県: "ishikawa", 福井県: "fukui", 山梨県: "yamanashi", 長野県: "nagano", 岐阜県: "gifu", 静岡県: "shizuoka", 愛知県: "aichi",
    三重県: "mie", 滋賀県: "shiga", 京都府: "kyoto", 大阪府: "osaka", 兵庫県: "hyogo", 奈良県: "nara", 和歌山県: "wakayama",
    鳥取県: "tottori", 島根県: "shimane", 岡山県: "okayama", 広島県: "hiroshima", 山口県: "yamaguchi", 徳島県: "tokushima", 香川県: "kagawa", 愛媛県: "ehime", 高知県: "kochi",
    福岡県: "fukuoka", 佐賀県: "saga", 長崎県: "nagasaki", 熊本県: "kumamoto", 大分県: "oita", 宮崎県: "miyazaki", 鹿児島県: "kagoshima", 沖縄県: "okinawa",
  };
  return map[name] || createHash("sha1").update(name).digest("hex").slice(0, 8);
}

function splitUnit(unit) {
  const match = unit.match(/^(.+?)（(.+)）$/);
  if (!match) return { shortUnit: unit, tags: [] };
  return { shortUnit: match[1], tags: match[2].split("・").map((value) => value.trim()).filter(Boolean) };
}

function pageNumber(name) {
  return Number(name.match(/(\d+)\.jpg$/i)?.[1] || 0);
}

function fail(message) {
  console.error(message);
  process.exit(1);
}
