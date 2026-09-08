"""高校入試 数学の大問抜粋PDFを作る。

理科版（koukou-nyushi-database の tmp/pdfs/batch_candidates/build_batch.py）を
基底として読み込み、教科を数学へ差し替えて使う。

レイアウト仕様の正本:
  koukou-nyushi-database/docs/高校入試_大問抜粋PDF作成・ページレイアウト手順.md

usage:
  python tools/extract/build_math.py              # 全件
  python tools/extract/build_math.py <slug> ...   # 指定スラッグのみ
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GITHUB = REPO.parent
BASE_BUILDER = Path(__file__).resolve().with_name("base_builder.py")

WORK_ROOT = REPO / "tmp" / "extract"
OUTPUT_ROOT = REPO / "output" / "pdf"
REVIEW_ROOT = WORK_ROOT / "review"
GENERATION_MANIFEST = REVIEW_ROOT / "generation-manifest.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from configs import CONFIGS  # noqa: E402


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def config_sha256(config: dict) -> str:
    payload = json.dumps(
        config, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def selected_configs() -> list[dict]:
    selected_slugs = set(sys.argv[1:])
    known = {config["slug"] for config in CONFIGS}
    unknown = selected_slugs - known
    if unknown:
        raise ValueError(f"Unknown slugs: {sorted(unknown)}")
    return [
        config
        for config in CONFIGS
        if not selected_slugs or config["slug"] in selected_slugs
    ]


def load_generation_manifest() -> dict:
    if not GENERATION_MANIFEST.exists():
        return {"schemaVersion": 1, "baseBuilderSha256": sha256(BASE_BUILDER), "items": {}}
    manifest = json.loads(GENERATION_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") != 1 or not isinstance(manifest.get("items"), dict):
        raise RuntimeError(f"生成履歴の形式が不正です: {GENERATION_MANIFEST}")
    return manifest


def write_generation_manifest(manifest: dict) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    temporary = GENERATION_MANIFEST.with_suffix(".tmp")
    temporary.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(GENERATION_MANIFEST)


def load_base_builder():
    spec = importlib.util.spec_from_file_location("excerpt_base", BASE_BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"基底ビルダーを読み込めません: {BASE_BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    selected = selected_configs()
    manifest = load_generation_manifest()
    builder_hash = sha256(BASE_BUILDER)
    if manifest.get("baseBuilderSha256") != builder_hash:
        # 基底を変えた後の部分生成で、旧基底のPDFが合格扱いにならないよう全件無効化する。
        manifest["items"] = {}
    manifest["baseBuilderSha256"] = builder_hash
    for config in selected:
        manifest["items"].pop(config["slug"], None)
    # PDFがWindowsでロックされて削除できない場合も、旧版を監査対象にしないよう
    # 生成履歴を先に無効化して永続化する。
    write_generation_manifest(manifest)
    for config in selected:
        review_pdf = (
            REVIEW_ROOT
            / f"中{config['grade']}数学_{config['field']}_確認中"
            / config["filename"]
        )
        review_pdf.unlink(missing_ok=True)

    batch = load_base_builder()
    batch.CONFIGS = CONFIGS
    # 理科版の基準（問題等800dpi・解答欄1200dpi以上）を満たしつつ、
    # 小さい切り出しをA4上で拡大しても実効600dpiを下回らない値にする。
    # 全22件の座標・配置倍率からの逆算値は、問題等811dpi、解答欄1947dpi。
    batch.SCIENCE_DPI = 820
    batch.ANSWER_DPI = 2000
    batch.WORK = WORK_ROOT / "build"
    batch.CROPS = batch.WORK / "crops"
    batch.STAGING = batch.WORK / "output"

    def source_paths(item: dict) -> tuple[Path, Path]:
        base = GITHUB / item["repo"] / "public" / "files" / str(item["year"])
        problem = base / "解説付き問題" / "数学.pdf"
        answer = base / "解答用紙" / "数学.pdf"
        if not problem.exists() or not answer.exists():
            raise FileNotFoundError(f"原本がありません: {problem} / {answer}")
        return problem, answer

    def source_line(item: dict) -> str:
        label = item.get("question_label") or f"大問{item['question']}"
        return f"{item['year']}年実施　{item['prefecture']}公立高校入試　数学　{label}"

    batch.source_paths = source_paths
    batch.source_line = source_line

    # 未監査のPDFを「最終版」へ直接入れない。まず監査用フォルダへ
    # 生成し、200〜240dpiの目視監査に合格したものだけを最終版へ移す。
    original_build_pdf = batch.build_pdf

    def build_pdf(config: dict, rendered: dict) -> dict:
        folder = REVIEW_ROOT / f"中{config['grade']}数学_{config['field']}_確認中"
        batch.PUBLISH = folder
        batch.CONTINUOUS = folder
        report = original_build_pdf(config, rendered)
        if report["minimum_effective_dpi"] < 600:
            raise RuntimeError(
                f"最小実効解像度が600dpi未満です: "
                f"{config['slug']} {report['minimum_effective_dpi']}dpi"
            )
        return report

    batch.build_pdf = build_pdf
    batch.PUBLISH = OUTPUT_ROOT
    batch.CONTINUOUS = OUTPUT_ROOT
    batch.main()

    reports = json.loads((batch.WORK / "build-report.json").read_text(encoding="utf-8"))
    if len(reports) != len(selected):
        raise RuntimeError(f"生成報告の件数が不正です: {len(reports)} != {len(selected)}")
    reports_by_filename = {
        Path(report["final_output"]).name: report for report in reports
    }
    source_hashes: dict[Path, str] = {}
    for config in selected:
        report = reports_by_filename.get(config["filename"])
        if report is None or not report.get("published"):
            raise RuntimeError(f"確認中PDFが確定していません: {config['slug']}")
        review_pdf = Path(report["final_output"])
        if not review_pdf.is_file() or report["minimum_effective_dpi"] < 600:
            raise RuntimeError(f"確認中PDFの生成結果が不正です: {config['slug']}")
        problem_pdf, answer_pdf = source_paths(config)
        for source in (problem_pdf, answer_pdf):
            if source not in source_hashes:
                source_hashes[source] = sha256(source)
        manifest["items"][config["slug"]] = {
            "filename": config["filename"],
            "pdfSha256": sha256(review_pdf),
            "configSha256": config_sha256(config),
            "problemSource": str(problem_pdf),
            "problemSourceSha256": source_hashes[problem_pdf],
            "answerSource": str(answer_pdf),
            "answerSourceSha256": source_hashes[answer_pdf],
            "minimumEffectiveDpi": report["minimum_effective_dpi"],
            "pages": report["pages"],
        }
    write_generation_manifest(manifest)


if __name__ == "__main__":
    main()
