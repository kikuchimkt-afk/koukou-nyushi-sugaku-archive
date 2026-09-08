"""確認中PDFを200dpiで全ページ画像化し、構成監査表を作る。

生成物は ``tmp/extract/audit`` に置く。PDFそのものには変更を加えない。
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[2]
REVIEW_ROOT = REPO / "tmp" / "extract" / "review"
AUDIT_ROOT = REPO / "tmp" / "extract" / "audit"
GENERATION_MANIFEST = REVIEW_ROOT / "generation-manifest.json"
BASE_BUILDER = Path(__file__).resolve().with_name("base_builder.py")
GITHUB = REPO.parent
DEFAULT_PDFTOPPM = Path(
    r"C:\Users\user\.cache\codex-runtimes\codex-primary-runtime"
    r"\dependencies\native\poppler\Library\bin\pdftoppm.exe"
)

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


def section_name(text: str, page_index: int) -> str:
    if page_index == 0 or text.startswith("問題") or "\n問題 " in text:
        return "problem"
    if text.startswith("解答用紙"):
        return "answer_sheet"
    if text.startswith("正解（全問）"):
        return "answers"
    if text.startswith("解説（"):
        return "explanation"
    return "unknown"


def make_contact_sheet(images: list[Path], destination: Path) -> None:
    thumb_width = 420
    gap = 18
    label_height = 30
    thumbnails: list[Image.Image] = []
    try:
        for image_path in images:
            with Image.open(image_path) as source:
                thumb_height = round(source.height * thumb_width / source.width)
                thumbnails.append(
                    source.convert("RGB").resize(
                        (thumb_width, thumb_height), Image.Resampling.LANCZOS
                    )
                )
        width = gap + sum(image.width + gap for image in thumbnails)
        height = gap + label_height + max(image.height for image in thumbnails) + gap
        sheet = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(sheet)
        x = gap
        for index, image in enumerate(thumbnails, 1):
            draw.text((x, gap), f"page {index}", fill="black")
            sheet.paste(image, (x, gap + label_height))
            x += image.width + gap
        sheet.save(destination, "JPEG", quality=88, optimize=True)
    finally:
        for image in thumbnails:
            image.close()


def main() -> None:
    pdftoppm = Path(os.environ.get("PDFTOPPM", str(DEFAULT_PDFTOPPM)))
    if not pdftoppm.exists():
        raise FileNotFoundError(f"pdftoppm がありません: {pdftoppm}")

    if not GENERATION_MANIFEST.is_file():
        raise FileNotFoundError(f"生成履歴がありません: {GENERATION_MANIFEST}")
    generation = json.loads(GENERATION_MANIFEST.read_text(encoding="utf-8"))
    if generation.get("schemaVersion") != 1 or not isinstance(generation.get("items"), dict):
        raise RuntimeError(f"生成履歴の形式が不正です: {GENERATION_MANIFEST}")
    builder_hash = sha256(BASE_BUILDER)
    if generation.get("baseBuilderSha256") != builder_hash:
        raise RuntimeError("生成後に基底ビルダーが変更されています。PDFを再生成してください。")

    expected = {config["filename"]: config for config in CONFIGS}
    expected_slugs = {config["slug"] for config in CONFIGS}
    if set(generation["items"]) != expected_slugs:
        missing = sorted(expected_slugs - set(generation["items"]))
        extra = sorted(set(generation["items"]) - expected_slugs)
        raise RuntimeError(f"生成履歴が22設定と一致しません: missing={missing} extra={extra}")
    pdfs = sorted(REVIEW_ROOT.rglob("*.pdf"), key=lambda path: path.name)
    names = [path.name for path in pdfs]
    if len(pdfs) != len(expected) or set(names) != set(expected):
        missing = sorted(set(expected) - set(names))
        extra = sorted(set(names) - set(expected))
        raise RuntimeError(
            f"確認中PDFが設定と一致しません: count={len(pdfs)} "
            f"missing={missing} extra={extra}"
        )

    AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    reports = []
    source_hashes: dict[Path, str] = {}
    allowed_order = ["problem", "answer_sheet", "answers", "explanation"]
    for index, pdf_path in enumerate(pdfs, 1):
        config = expected[pdf_path.name]
        generated = generation["items"][config["slug"]]
        pdf_hash = sha256(pdf_path)
        if generated.get("filename") != config["filename"]:
            raise RuntimeError(f"生成履歴のファイル名が不一致です: {config['slug']}")
        if generated.get("pdfSha256") != pdf_hash:
            raise RuntimeError(f"生成後にPDFが変更されています: {config['slug']}")
        if generated.get("configSha256") != config_sha256(config):
            raise RuntimeError(f"生成後に設定が変更されています: {config['slug']}")
        source_base = (
            GITHUB / config["repo"] / "public" / "files" / str(config["year"])
        )
        problem_source = source_base / "解説付き問題" / "数学.pdf"
        answer_source = source_base / "解答用紙" / "数学.pdf"
        source_expectations = (
            ("problemSource", "problemSourceSha256", problem_source),
            ("answerSource", "answerSourceSha256", answer_source),
        )
        for path_key, hash_key, source_path in source_expectations:
            if generated.get(path_key) != str(source_path):
                raise RuntimeError(f"生成履歴の原本パスが不一致です: {config['slug']}")
            if not source_path.is_file():
                raise RuntimeError(f"原本がありません: {config['slug']} {source_path}")
            if source_path not in source_hashes:
                source_hashes[source_path] = sha256(source_path)
            if generated.get(hash_key) != source_hashes[source_path]:
                raise RuntimeError(f"生成後に原本が変更されています: {config['slug']}")
        if generated.get("minimumEffectiveDpi", 0) < 600:
            raise RuntimeError(f"実効解像度が600dpi未満です: {config['slug']}")
        reader = PdfReader(str(pdf_path))
        if generated.get("pages") != len(reader.pages):
            raise RuntimeError(f"生成履歴のページ数が不一致です: {config['slug']}")
        sections = []
        sizes = []
        for page_index, page in enumerate(reader.pages):
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if not (
                abs(width - 595.276) <= 0.25 and abs(height - 841.89) <= 0.25
            ):
                raise RuntimeError(f"A4縦でないページ: {pdf_path.name} p{page_index + 1}")
            sizes.append([round(width, 3), round(height, 3)])
            sections.append(section_name(page.extract_text() or "", page_index))

        compact = []
        for section in sections:
            if not compact or compact[-1] != section:
                compact.append(section)
        if compact != allowed_order or sections.count("answer_sheet") != 1:
            raise RuntimeError(
                f"構成順が不正: {pdf_path.name} sections={sections} compact={compact}"
            )

        page_dir = AUDIT_ROOT / config["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        for old_image in page_dir.glob("page-*.jpg"):
            old_image.unlink()
        prefix = page_dir / "render"
        command = [
            str(pdftoppm),
            "-jpeg",
            "-r",
            "200",
            "-jpegopt",
            "quality=82,optimize=y,progressive=y",
            "-q",
            str(pdf_path),
            str(prefix),
        ]
        subprocess.run(command, check=True)
        rendered = sorted(
            page_dir.glob("render-*.jpg"),
            key=lambda path: int(path.stem.rsplit("-", 1)[1]),
        )
        if len(rendered) != len(reader.pages):
            raise RuntimeError(f"監査画像のページ数不一致: {pdf_path.name}")
        page_images = []
        for page_number, source in enumerate(rendered, 1):
            destination = page_dir / f"page-{page_number:02d}.jpg"
            source.replace(destination)
            page_images.append(destination)
        contact_path = AUDIT_ROOT / f"{config['slug']}-contact.jpg"
        make_contact_sheet(page_images, contact_path)
        reports.append(
            {
                "slug": config["slug"],
                "pdf": str(pdf_path),
                "pages": len(reader.pages),
                "sections": sections,
                "pageSizes": sizes,
                "sha256": pdf_hash,
                "renderDpi": 200,
                "pageImages": [str(path) for path in page_images],
                "contactSheet": str(contact_path),
            }
        )
        print(f"[{index}/{len(pdfs)}] {config['slug']} {len(reader.pages)}p {sections}")

    manifest_path = AUDIT_ROOT / "manifest.json"
    manifest_path.write_text(
        json.dumps({"pdfs": reports}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"OK: {len(reports)} PDFs / {sum(item['pages'] for item in reports)} pages")
    print(manifest_path)


if __name__ == "__main__":
    main()
