import { createHash } from "node:crypto";
import { access, readFile, readdir, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const repoRoot = path.resolve(import.meta.dirname, "..");
const data = JSON.parse(await readFile(path.join(repoRoot, "data", "archive.generated.json"), "utf8"));
const errors = [];
const ids = new Set();
const releaseNames = new Set();
// 収録を追加したら、ここと EXPECTED_TOTALS を更新する。
// 値は data/archive.generated.json を機械集計して合わせること。
const expectedCounts = new Map([
  ["1:データの活用", 4],
  ["2:数と式", 1],
  ["2:方程式の利用", 1],
  ["2:規則性", 3],
  ["2:関数", 8],
  ["2:図形の証明", 2],
  ["2:データの活用", 3],
]);
const EXPECTED_TOTALS = { releaseTag: "pdfs-v1", items: 22, pages: 102 };
const VALID_FIELDS = new Set([
  "数と式",
  "方程式",
  "方程式の利用",
  "規則性",
  "関数",
  "図形",
  "図形の証明",
  "データの活用",
]);
const actualCounts = new Map();

for (const item of data.items) {
  if (ids.has(item.id)) errors.push(`重複ID: ${item.id}`);
  ids.add(item.id);
  const countKey = `${item.grade}:${item.field}`;
  actualCounts.set(countKey, (actualCounts.get(countKey) || 0) + 1);
  const releaseName = `${item.id}.pdf`;
  const releasePath = path.join(repoRoot, ".release-assets", releaseName);
  releaseNames.add(releaseName);
  if (!/^[a-f0-9]{64}$/.test(item.contentVersion || "")) {
    errors.push(`PDF内容版が不正: ${item.id} ${item.contentVersion || "(なし)"}`);
  }
  try {
    const releaseInfo = await stat(releasePath);
    if (releaseInfo.size !== item.fileSize) {
      errors.push(`PDFサイズ不一致: ${releaseName} ${releaseInfo.size} != ${item.fileSize}`);
    }
    const actualVersion = createHash("sha256").update(await readFile(releasePath)).digest("hex");
    if (actualVersion !== item.contentVersion) {
      errors.push(`PDF内容版不一致: ${releaseName} ${actualVersion} != ${item.contentVersion}`);
    }
  } catch {
    errors.push(`PDFなし: ${releaseName}`);
  }
  if (!item.pdfUrl.endsWith(`?rev=${item.contentVersion}`)) {
    errors.push(`PDF URLの内容版不一致: ${item.id}`);
  }
  if (!item.previewPages.length) errors.push(`プレビューなし: ${item.id}`);
  for (const preview of item.previewPages) {
    if (!preview.endsWith(`?v=${item.contentVersion}`)) {
      errors.push(`プレビューURLの内容版不一致: ${preview}`);
    }
    const previewPath = preview.split("?", 1)[0];
    const filePath = path.join(repoRoot, "public", previewPath.replace(/^\//, ""));
    try {
      await access(filePath);
      const info = await stat(filePath);
      if (info.size < 10_000) errors.push(`画像が小さすぎます: ${preview}`);
    } catch {
      errors.push(`画像なし: ${preview}`);
    }
  }
}

for (const entry of await readdir(path.join(repoRoot, "public", "previews"), { withFileTypes: true })) {
  if (entry.isDirectory() && /^g[123]-/.test(entry.name) && !ids.has(entry.name)) {
    errors.push(`古いプレビュー: ${entry.name}`);
  }
}
for (const entry of await readdir(path.join(repoRoot, ".release-assets"), { withFileTypes: true })) {
  if (entry.isFile() && /^g[123]-.+\.pdf$/i.test(entry.name) && !releaseNames.has(entry.name)) {
    errors.push(`古いPDF: ${entry.name}`);
  }
}

const countedPages = data.items.reduce((sum, item) => sum + item.previewPages.length, 0);
if (countedPages !== data.totalPages) errors.push(`ページ数不一致: ${countedPages} != ${data.totalPages}`);
if (data.items.length !== data.totalItems) errors.push(`題数不一致: ${data.items.length} != ${data.totalItems}`);
if (data.releaseTag !== EXPECTED_TOTALS.releaseTag) {
  errors.push(`公開PDF版不一致: ${data.releaseTag} != ${EXPECTED_TOTALS.releaseTag}`);
}
if (EXPECTED_TOTALS.items !== null && data.totalItems !== EXPECTED_TOTALS.items) {
  errors.push(`公開予定題数不一致: ${data.totalItems} != ${EXPECTED_TOTALS.items}`);
}
if (EXPECTED_TOTALS.pages !== null && data.totalPages !== EXPECTED_TOTALS.pages) {
  errors.push(`公開予定ページ数不一致: ${data.totalPages} != ${EXPECTED_TOTALS.pages}`);
}
for (const [key, expected] of expectedCounts) {
  const actual = actualCounts.get(key) || 0;
  if (actual !== expected) errors.push(`領域別題数不一致: ${key} ${actual} != ${expected}`);
}
for (const [key, actual] of actualCounts) {
  const field = key.split(":")[1];
  if (!VALID_FIELDS.has(field)) errors.push(`想定外の領域: ${key} ${actual}題`);
  if (expectedCounts.size && !expectedCounts.has(key)) {
    errors.push(`想定外の学年・領域: ${key} ${actual}題`);
  }
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(`OK: ${data.totalItems}題 / ${data.totalPages}ページ / ID重複なし / 全画像・全PDFあり / 古い生成物なし`);
