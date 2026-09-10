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

from PIL import Image

REPO = Path(__file__).resolve().parents[2]
BASE_BUILDER = Path(__file__).resolve().with_name("base_builder.py")
MANIFEST_SCHEMA_VERSION = 1

WORK_ROOT = REPO / "tmp" / "extract"
OUTPUT_ROOT = REPO / "output" / "pdf"
REVIEW_ROOT = WORK_ROOT / "review"
GENERATION_MANIFEST = REVIEW_ROOT / "generation-manifest.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from configs import CONFIGS  # noqa: E402
from generation_contract import pipeline_sha256  # noqa: E402
from source_paths import section_source_path, source_paths  # noqa: E402


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


def selected_configs(generated_slugs: set[str]) -> list[dict]:
    arguments = sys.argv[1:]
    if arguments == ["--missing"]:
        return [config for config in CONFIGS if config["slug"] not in generated_slugs]
    if "--missing" in arguments:
        raise ValueError("--missing は他のスラッグと同時指定できません")
    selected_slugs = set(arguments)
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
        return {
            "schemaVersion": MANIFEST_SCHEMA_VERSION,
            "baseBuilderSha256": sha256(BASE_BUILDER),
            "items": {},
        }
    manifest = json.loads(GENERATION_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") != MANIFEST_SCHEMA_VERSION or not isinstance(
        manifest.get("items"), dict
    ):
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
    manifest = load_generation_manifest()
    selected = selected_configs(set(manifest["items"]))
    if not selected:
        print("生成対象はありません。")
        return
    builder_hash = sha256(BASE_BUILDER)
    pipeline_hash = pipeline_sha256()
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
    batch.CONFIGS = selected
    # 理科版の基準（問題等800dpi・解答欄1200dpi以上）を満たしつつ、
    # 小さい切り出しをA4上で拡大しても実効600dpiを下回らない値にする。
    # 既存22件の逆算下限811dpiに加え、沖縄県の短い正解断片を拡大する
    # 構成でも余裕を持たせるため、問題・正解・解説は850dpiとする。
    batch.SCIENCE_DPI = 850
    batch.ANSWER_DPI = 2100
    batch.WORK = WORK_ROOT / "build"
    batch.CROPS = batch.WORK / "crops"
    batch.STAGING = batch.WORK / "output"

    def source_line(item: dict) -> str:
        label = item.get("question_label") or f"大問{item['question']}"
        session = f"（{item['session']}）" if item.get("session") else ""
        return (
            f"{item['year']}年実施　{item['prefecture']}公立高校入試"
            f"{session}　数学　{label}"
        )

    batch.source_paths = source_paths
    batch.source_line = source_line

    # 一部のローカル原本（岩手県2021・2022年）は、問題PDFと解説PDFが
    # 分かれている。固定した理科版基底を変更せず、該当設定だけ解説cropを
    # 別原本から差し替える。既存22題の基底ハッシュと監査履歴は維持される。
    original_render_config = batch.render_config

    def apply_white_masks(rendered_item: dict, masks: list[list[float]]) -> None:
        """対象本文を残したまま、正規化座標で隣接大問の断片だけを白くする。"""
        if not masks:
            return
        rendered_path = Path(rendered_item["path"])
        with Image.open(rendered_path) as source:
            masked = source.convert("L")
            width, height = masked.size
            for mask in masks:
                if (
                    len(mask) != 4
                    or not all(isinstance(value, (int, float)) for value in mask)
                ):
                    raise ValueError(f"white_masks の形式が不正です: {mask}")
                left, top, right, bottom = mask
                if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
                    raise ValueError(f"white_masks の範囲が不正です: {mask}")
                box = (
                    max(0, round(left * width)),
                    max(0, round(top * height)),
                    min(width, round(right * width)),
                    min(height, round(bottom * height)),
                )
                masked.paste(255, box)
            masked.save(
                rendered_path,
                format="JPEG",
                quality=97,
                subsampling=0,
                optimize=True,
            )

    def render_config(config: dict) -> dict:
        explanation_override = config.get("explanation_source_pdf")
        if not explanation_override:
            rendered = original_render_config(config)
        else:
            config_without_explanation = dict(config)
            config_without_explanation["explanation"] = []
            rendered = original_render_config(config_without_explanation)
            problem_pdf, _ = source_paths(config)
            explanation_pdf = section_source_path(config, "explanation", problem_pdf)
            config_dir = batch.CROPS / config["slug"]
            science_dpi = config.get("science_dpi", batch.SCIENCE_DPI)
            default_ref = config.get("explanation_ref", config["science_ref"])
            for index, item in enumerate(config["explanation"], 1):
                rendered["explanation"].append(
                    batch.render_crop(
                        explanation_pdf,
                        item["page"],
                        item["box"],
                        tuple(item.get("ref_size", default_ref)),
                        science_dpi,
                        config_dir / f"explanation-{index}.jpg",
                    )
                )

        # 解答・解説原本では、対象本文の横へ前後大問の図が回り込む場合が
        # ある。矩形cropを狭めて本文を欠かす代わりに、設定された範囲だけ
        # 白くして対象大問の情報を完全に残す。
        for section in ("answers", "explanation"):
            if len(rendered[section]) != len(config[section]):
                raise RuntimeError(
                    f"{section} の描画件数が設定と一致しません: {config['slug']}"
                )
            for source_item, rendered_item in zip(config[section], rendered[section]):
                apply_white_masks(rendered_item, source_item.get("white_masks", []))
        return rendered

    batch.render_config = render_config

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
    source_hashes: dict[Path, str] = {}
    original_argv = sys.argv
    for index, config in enumerate(selected, 1):
        print(f"[{index}/{len(selected)}] {config['slug']}")
        try:
            # 1題ごとに生成・履歴保存する。後続題で停止しても、
            # 合格済みPDFの履歴を失わず --missing で再開できる。
            batch.CONFIGS = [config]
            # 基底側へは既に絞り込んだCONFIGSだけを渡し、特殊オプションや
            # 長いスラッグ列を再解釈させない。
            sys.argv = [sys.argv[0]]
            batch.main()
        finally:
            sys.argv = original_argv

        reports = json.loads(
            (batch.WORK / "build-report.json").read_text(encoding="utf-8")
        )
        if len(reports) != 1:
            raise RuntimeError(f"生成報告の件数が不正です: {len(reports)} != 1")
        report = reports[0]
        if Path(report["final_output"]).name != config["filename"]:
            raise RuntimeError(f"生成報告の対象が不正です: {config['slug']}")
        if report is None or not report.get("published"):
            raise RuntimeError(f"確認中PDFが確定していません: {config['slug']}")
        review_pdf = Path(report["final_output"])
        if not review_pdf.is_file() or report["minimum_effective_dpi"] < 600:
            raise RuntimeError(f"確認中PDFの生成結果が不正です: {config['slug']}")
        problem_pdf, answer_pdf = source_paths(config)
        answers_pdf = section_source_path(config, "answers", problem_pdf)
        explanation_pdf = section_source_path(config, "explanation", problem_pdf)
        for source in (problem_pdf, answer_pdf, answers_pdf, explanation_pdf):
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
            "answersSource": str(answers_pdf),
            "answersSourceSha256": source_hashes[answers_pdf],
            "explanationSource": str(explanation_pdf),
            "explanationSourceSha256": source_hashes[explanation_pdf],
            "pipelineSha256": pipeline_hash,
            "minimumEffectiveDpi": report["minimum_effective_dpi"],
            "pages": report["pages"],
        }
        write_generation_manifest(manifest)


if __name__ == "__main__":
    main()
