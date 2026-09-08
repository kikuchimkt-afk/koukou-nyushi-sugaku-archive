"""理科版の確定レイアウト実装を数学用に固定したローカル基底。

元ファイル: koukou-nyushi-database/tmp/pdfs/batch_candidates/build_batch.py
元ファイルSHA-256: 5eb962ac08e30446d81cadd2a0626287175c2eded1c7cedf0a594d133d19a797
理科固有のCONFIGSだけを除き、描画・配置・解像度計算は同一に保つ。
"""

from __future__ import annotations

import json
import math
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


DATABASE = Path(r"C:\Users\user\Documents\GitHub\koukou-nyushi-database")
GITHUB = Path(r"C:\Users\user\Documents\GitHub")
OUTPUT = DATABASE / "output" / "pdf"
PUBLISH = OUTPUT / "中1理科_地学生物_最終版"
CONTINUOUS = PUBLISH
WORK = DATABASE / "tmp" / "pdfs" / "batch_candidates" / "build"
CROPS = WORK / "crops"
STAGING = WORK / "output"
POPPLER = Path(
    r"C:\Users\user\.cache\codex-runtimes\codex-primary-runtime"
    r"\dependencies\native\poppler\Library\bin\pdftoppm.exe"
)
FONT_REGULAR = Path(r"C:\Windows\Fonts\BIZ-UDGothicR.ttc")
FONT_BOLD = Path(r"C:\Windows\Fonts\BIZ-UDGothicB.ttc")

SCIENCE_DPI = 800
ANSWER_DPI = 1200
A4_WIDTH, A4_HEIGHT = A4
PAGE_MARGIN = 35
CONTENT_WIDTH = A4_WIDTH - PAGE_MARGIN * 2
CONTENT_BOTTOM = 40
CONTENT_TOP = 775
SOURCE_PAGE_PT = (515.9, 728.5)
PROBLEM_MIN_SCALE = 0.85
PROBLEM_GAP = 3


def box(x1: int, y1: int, x2: int, y2: int) -> list[int]:
    return [x1, y1, x2, y2]


CONFIGS: list[dict] = []


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("BIZUD", str(FONT_REGULAR)))
    pdfmetrics.registerFont(TTFont("BIZUDB", str(FONT_BOLD)))


def ensure_tools() -> None:
    required = [POPPLER, FONT_REGULAR, FONT_BOLD]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)


def source_paths(config: dict) -> tuple[Path, Path]:
    year = config.get("year", 2024)
    base = GITHUB / config["repo"] / "public" / "files" / str(year)
    science_override = config.get("science_source_pdf")
    science = Path(science_override) if science_override else base / "解説付き問題" / "理科.pdf"
    if not science.is_absolute():
        science = DATABASE / science
    answer = base / "解答用紙" / "理科.pdf"
    if not science.exists() or not answer.exists():
        raise FileNotFoundError(f"Source missing: {science} / {answer}")
    return science, answer


def source_box_for_rotation(
    upright_box: list[int], rotation: int | str, source_ref: tuple[int, int]
) -> list[int]:
    x1, y1, x2, y2 = upright_box
    source_w, source_h = source_ref
    if rotation == "cw":
        return [y1, source_h - x2, y2, source_h - x1]
    if rotation == "ccw":
        return [source_w - y2, x1, source_w - y1, x2]
    return upright_box


def render_crop(
    pdf_path: Path,
    page: int,
    requested_box: list[int],
    ref_size: tuple[int, int],
    dpi: int,
    destination: Path,
    rotation: int | str = 0,
) -> dict:
    source_box = source_box_for_rotation(requested_box, rotation, ref_size)
    ref_w, ref_h = ref_size
    x1, y1, x2, y2 = source_box
    scale = dpi / 150.0
    crop_x = max(0, math.floor(x1 * scale))
    crop_y = max(0, math.floor(y1 * scale))
    crop_w = max(1, math.ceil((x2 - x1) * scale))
    crop_h = max(1, math.ceil((y2 - y1) * scale))
    prefix = destination.with_suffix("")
    png_path = prefix.with_suffix(".png")
    if png_path.exists():
        png_path.unlink()
    cmd = [
        str(POPPLER),
        "-f",
        str(page),
        "-l",
        str(page),
        "-singlefile",
        "-gray",
        "-png",
        "-r",
        str(dpi),
        "-x",
        str(crop_x),
        "-y",
        str(crop_y),
        "-W",
        str(crop_w),
        "-H",
        str(crop_h),
        str(pdf_path),
        str(prefix),
    ]
    # Very high-DPI crops occasionally make pdftoppm fail once on Windows even
    # though the same command succeeds immediately afterwards. Retry a small,
    # fixed number of times so a transient renderer failure is not mistaken for
    # an invalid crop definition. A persistent failure still raises normally.
    for attempt in range(3):
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            break
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise
            png_path.unlink(missing_ok=True)
            time.sleep(0.5 * (attempt + 1))
    with Image.open(png_path) as image:
        rendered = image.convert("L")
        if rotation == "cw":
            rendered = rendered.transpose(Image.Transpose.ROTATE_270)
        elif rotation == "ccw":
            rendered = rendered.transpose(Image.Transpose.ROTATE_90)
        rendered.save(destination, format="JPEG", quality=97, subsampling=0, optimize=True)
        width, height = rendered.size
    png_path.unlink(missing_ok=True)
    return {
        "path": str(destination),
        "pixels": [width, height],
        "dpi": dpi,
        "page": page,
        "requested_box": requested_box,
        "source_box": source_box,
        "ref_size": [ref_w, ref_h],
        "rotation": rotation,
    }


def render_config(config: dict) -> dict:
    science_pdf, answer_pdf = source_paths(config)
    answers_source = Path(config.get("answers_source_pdf", science_pdf))
    if not answers_source.is_absolute():
        answers_source = DATABASE / answers_source
    if not answers_source.exists():
        raise FileNotFoundError(
            f"Supplemental answer source missing for {config['slug']}: {answers_source}"
        )
    config_dir = CROPS / config["slug"]
    config_dir.mkdir(parents=True, exist_ok=True)
    rendered = {"problem": [], "answer_sheet": [], "answers": [], "explanation": []}
    science_dpi = config.get("science_dpi", SCIENCE_DPI)
    for index, item in enumerate(config["problem"], 1):
        rendered["problem"].append(
            render_crop(
                science_pdf,
                item["page"],
                item["box"],
                tuple(item.get("ref_size", config["science_ref"])),
                science_dpi,
                config_dir / f"problem-{index}.jpg",
            )
        )
    for index, item in enumerate(config["answer_sheet"], 1):
        answer_item = render_crop(
            answer_pdf,
            item.get("page", 1),
            item["box"],
            tuple(
                item.get(
                    "source_ref_size",
                    item.get("ref_size", (1075, 1518)),
                )
            ),
            ANSWER_DPI,
            config_dir / f"answer-sheet-{index}.jpg",
            item.get("rotation", 0),
        )
        # Some official answer sheets place scoring boxes immediately beside a
        # question.  A rectangular source crop can then retain a tiny fragment
        # even when every target field is necessary.  Optional masks use
        # normalized coordinates within the rendered crop and cover only those
        # unrelated fragments with white, preserving the printable field.
        if item.get("white_masks"):
            answer_path = Path(answer_item["path"])
            with Image.open(answer_path) as source:
                masked = source.convert("L")
                width, height = masked.size
                for left, top, right, bottom in item["white_masks"]:
                    box = (
                        max(0, round(left * width)),
                        max(0, round(top * height)),
                        min(width, round(right * width)),
                        min(height, round(bottom * height)),
                    )
                    masked.paste(255, box)
                masked.save(
                    answer_path,
                    format="JPEG",
                    quality=97,
                    subsampling=0,
                    optimize=True,
                )
        rendered["answer_sheet"].append(answer_item)
    for section in ("answers", "explanation"):
        for index, item in enumerate(config[section], 1):
            section_pdf = answers_source if section == "answers" else science_pdf
            default_ref = (
                config.get("answers_ref", config["science_ref"])
                if section == "answers"
                else config["science_ref"]
            )
            rendered[section].append(
                render_crop(
                    section_pdf,
                    item["page"],
                    item["box"],
                    tuple(item.get("ref_size", default_ref)),
                    science_dpi,
                    config_dir / f"{section}-{index}.jpg",
                )
            )
    return rendered


def problem_capacity(page_index: int) -> float:
    return (782 if page_index == 0 else CONTENT_TOP) - CONTENT_BOTTOM


def capacity_for_pages(page_count: int) -> float:
    if page_count <= 0:
        return 0
    return problem_capacity(0) + problem_capacity(1) * (page_count - 1)


def choose_problem_flow_scale(items: list[dict]) -> tuple[float, int]:
    aspect_sum = 0.0
    for item in items:
        px_w, px_h = item["pixels"]
        aspect_sum += px_h / px_w
    fixed_gaps = PROBLEM_GAP * max(0, len(items) - 1)

    height_at_minimum = CONTENT_WIDTH * PROBLEM_MIN_SCALE * aspect_sum + fixed_gaps
    minimum_pages = 1
    while capacity_for_pages(minimum_pages) + 0.1 < height_at_minimum:
        minimum_pages += 1

    largest_scale = (
        capacity_for_pages(minimum_pages) - fixed_gaps
    ) / (CONTENT_WIDTH * aspect_sum)
    return max(PROBLEM_MIN_SCALE, min(1.0, largest_scale)), minimum_pages


def find_whitespace_break(image: Image.Image, ideal: int, lower: int, upper: int) -> int:
    lower = max(lower, 1)
    upper = min(upper, image.height - 1)
    ideal = max(lower, min(ideal, upper))
    if lower >= upper:
        return ideal
    sample = image.crop((0, lower, image.width, upper + 1)).convert("L")
    sample_width = min(500, max(100, image.width // 10))
    sample = sample.resize((sample_width, sample.height), Image.Resampling.BILINEAR)
    pixels = sample.load()
    blank_rows: list[tuple[int, int]] = []
    best_row = ideal
    best_brightness = -1.0
    for local_y in range(sample.height):
        brightness = sum(pixels[x, local_y] for x in range(sample_width)) / sample_width
        absolute_y = lower + local_y
        if brightness >= 251.5:
            blank_rows.append((abs(absolute_y - ideal), absolute_y))
        if brightness > best_brightness:
            best_brightness = brightness
            best_row = absolute_y
    if blank_rows:
        blank_rows.sort()
        return blank_rows[0][1]
    return best_row


def save_problem_slice(
    source_path: str,
    start_y: int,
    end_y: int,
    destination: Path,
) -> tuple[int, int]:
    with Image.open(source_path) as image:
        if start_y == 0 and end_y == image.height:
            shutil.copyfile(source_path, destination)
            return image.width, image.height
        sliced = image.crop((0, start_y, image.width, end_y)).convert("L")
        sliced.save(destination, format="JPEG", quality=97, subsampling=0, optimize=True)
        return sliced.size


def prepare_problem_flow(config: dict, rendered: dict) -> None:
    items = rendered["problem"]
    page_groups = config.get("problem_page_groups")
    if page_groups is not None:
        problem_gap = config.get("problem_gap", PROBLEM_GAP)
        if problem_gap < 0:
            raise ValueError("problem_gap must not be negative")
        flattened = [item_number for group in page_groups for item_number in group]
        expected = list(range(1, len(items) + 1))
        if flattened != expected:
            raise ValueError(
                "problem_page_groups must contain every problem fragment exactly once "
                "in source order"
            )

        scale_cap = config.get("problem_scale_cap", 1.0)
        if scale_cap < PROBLEM_MIN_SCALE or scale_cap > 1.0:
            raise ValueError(
                f"problem_scale_cap must be between {PROBLEM_MIN_SCALE} and 1.0"
            )
        flow_scale = scale_cap
        for page_index, group in enumerate(page_groups):
            aspect_sum = sum(
                items[item_number - 1]["pixels"][1]
                / items[item_number - 1]["pixels"][0]
                for item_number in group
            )
            fixed_gaps = problem_gap * max(0, len(group) - 1)
            available = problem_capacity(page_index) - fixed_gaps
            flow_scale = min(flow_scale, available / (CONTENT_WIDTH * aspect_sum))
        if flow_scale + 1e-9 < PROBLEM_MIN_SCALE:
            raise RuntimeError(
                f"Forced problem page groups require scale {flow_scale:.3f}, below "
                f"the allowed minimum {PROBLEM_MIN_SCALE:.2f} for {config['slug']}"
            )

        draw_width = CONTENT_WIDTH * flow_scale
        pages: list[list[dict]] = []
        for group in page_groups:
            page_slices: list[dict] = []
            for group_index, item_number in enumerate(group):
                item = items[item_number - 1]
                page_slices.append(
                    {
                        "path": item["path"],
                        "pixels": item["pixels"],
                        "draw_width": draw_width,
                        "gap_before": problem_gap if group_index else 0,
                    }
                )
            pages.append(page_slices)
        rendered["problem_flow"] = pages
        rendered["problem_flow_scale"] = flow_scale
        return

    flow_scale, page_count = choose_problem_flow_scale(items)
    scale_cap = config.get("problem_scale_cap")
    if scale_cap is not None:
        if scale_cap < PROBLEM_MIN_SCALE or scale_cap > 1.0:
            raise ValueError(
                f"problem_scale_cap must be between {PROBLEM_MIN_SCALE} and 1.0"
            )
        flow_scale = min(flow_scale, scale_cap)
    draw_width = CONTENT_WIDTH * flow_scale
    remaining_total = sum(
        item["pixels"][1] / item["pixels"][0] * draw_width for item in items
    ) + PROBLEM_GAP * max(0, len(items) - 1)
    pages: list[list[dict]] = []
    item_index = 0
    item_start_y = 0
    slice_index = 1
    flow_dir = CROPS / config["slug"] / "flow"
    flow_dir.mkdir(parents=True, exist_ok=True)

    for page_index in range(page_count):
        capacity = problem_capacity(page_index)
        pages_left = page_count - page_index
        target_height = min(capacity, remaining_total / pages_left)
        used = 0.0
        page_slices: list[dict] = []

        while item_index < len(items):
            item = items[item_index]
            px_w, px_h = item["pixels"]
            remaining_px = px_h - item_start_y
            remaining_height = remaining_px / px_w * draw_width
            gap = PROBLEM_GAP if page_slices and item_start_y == 0 else 0
            room_to_target = target_height - used - gap
            room_to_capacity = capacity - used - gap

            if remaining_height <= room_to_target + 0.25 or page_index == page_count - 1:
                destination = flow_dir / f"flow-{slice_index:02d}.jpg"
                slice_w, slice_h = save_problem_slice(
                    item["path"], item_start_y, px_h, destination
                )
                page_slices.append(
                    {
                        "path": str(destination),
                        "pixels": [slice_w, slice_h],
                        "draw_width": draw_width,
                        "gap_before": gap,
                    }
                )
                slice_index += 1
                used += gap + remaining_height
                remaining_total -= gap + remaining_height
                item_index += 1
                item_start_y = 0
                if used >= target_height - 0.25:
                    break
                continue

            if room_to_target <= 10 or room_to_capacity <= 10:
                break

            ideal_px = item_start_y + int(room_to_target / draw_width * px_w)
            max_px = item_start_y + int(room_to_capacity / draw_width * px_w)
            search_radius = max(80, int(px_w * 0.055))
            lower = max(item_start_y + 80, ideal_px - search_radius)
            upper = min(px_h - 80, ideal_px + search_radius, max_px)
            with Image.open(item["path"]) as image:
                break_y = find_whitespace_break(image, ideal_px, lower, upper)
            if break_y <= item_start_y + 20:
                break
            destination = flow_dir / f"flow-{slice_index:02d}.jpg"
            slice_w, slice_h = save_problem_slice(
                item["path"], item_start_y, break_y, destination
            )
            draw_height = slice_h / slice_w * draw_width
            page_slices.append(
                {
                    "path": str(destination),
                    "pixels": [slice_w, slice_h],
                    "draw_width": draw_width,
                    "gap_before": gap,
                }
            )
            slice_index += 1
            used += gap + draw_height
            remaining_total -= gap + draw_height
            item_start_y = break_y
            break

        if not page_slices:
            raise RuntimeError(f"Unable to paginate problem flow for {config['slug']}")
        pages.append(page_slices)

    if item_index != len(items) or item_start_y != 0:
        raise RuntimeError(f"Problem flow left unplaced content for {config['slug']}")
    rendered["problem_flow"] = pages
    rendered["problem_flow_scale"] = flow_scale


def prepare_raster_flow(items: list[dict]) -> list[list[dict]]:
    if len(items) <= 1:
        return [[{**items[0], "draw_width": CONTENT_WIDTH}]] if items else []
    aspect_sum = sum(item["pixels"][1] / item["pixels"][0] for item in items)
    fixed_gaps = PROBLEM_GAP * (len(items) - 1)
    available_height = CONTENT_TOP - CONTENT_BOTTOM
    largest_scale = min(
        1.0,
        (available_height - fixed_gaps) / (CONTENT_WIDTH * aspect_sum),
    )
    if largest_scale >= PROBLEM_MIN_SCALE:
        draw_width = CONTENT_WIDTH * largest_scale
        return [[{**item, "draw_width": draw_width} for item in items]]
    return [[{**item, "draw_width": CONTENT_WIDTH}] for item in items]


def source_line(config: dict) -> str:
    year = config.get("year", 2024)
    return f"{year}年実施　{config['prefecture']}公立高校入試　理科　大問{config['question']}"


def draw_footer(
    pdf: canvas.Canvas,
    page_number: int,
    total_pages: int,
    page_width: float = A4_WIDTH,
    y: float = 17,
) -> None:
    pdf.setFillColor(HexColor("#333333"))
    pdf.setFont("BIZUD", 7)
    pdf.drawCentredString(page_width / 2, y, f"{page_number} / {total_pages}")


def draw_rule(pdf: canvas.Canvas, y: float = 786, page_width: float = A4_WIDTH) -> None:
    pdf.setStrokeColor(HexColor("#303030"))
    pdf.setLineWidth(0.55)
    pdf.line(PAGE_MARGIN, y, page_width - PAGE_MARGIN, y)


def draw_standard_header(
    pdf: canvas.Canvas,
    title: str,
    config: dict,
    page_width: float = A4_WIDTH,
    page_height: float = A4_HEIGHT,
) -> None:
    # Preserve the original integer coordinates on portrait A4.  Computing
    # these as A4_HEIGHT offsets introduces 0.11pt sub-pixel shifts and changes
    # otherwise untouched pages during raster verification.
    portrait_a4 = abs(page_width - A4_WIDTH) <= 0.2 and abs(page_height - A4_HEIGHT) <= 0.2
    if portrait_a4:
        title_y, source_y, rule_y = 804, 807, 786
    else:
        title_y = page_height - 38
        source_y = page_height - 35
        rule_y = page_height - 56
    pdf.setFillColor(HexColor("#171717"))
    pdf.setFont("BIZUDB", 16)
    pdf.drawString(PAGE_MARGIN, title_y, title)
    pdf.setFont("BIZUD", 7)
    pdf.drawRightString(page_width - PAGE_MARGIN, source_y, source_line(config))
    draw_rule(pdf, rule_y, page_width)


def fit_image_size(image_path: str, max_width: float, max_height: float) -> tuple[float, float, float]:
    with Image.open(image_path) as image:
        px_w, px_h = image.size
    factor = min(max_width / px_w, max_height / px_h)
    draw_w = px_w * factor
    draw_h = px_h * factor
    effective_dpi = min(px_w / (draw_w / 72), px_h / (draw_h / 72))
    return draw_w, draw_h, effective_dpi


def draw_fitted_image(
    pdf: canvas.Canvas,
    image_path: str,
    top: float = CONTENT_TOP,
    bottom: float = CONTENT_BOTTOM,
) -> float:
    draw_w, draw_h, effective_dpi = fit_image_size(
        image_path, CONTENT_WIDTH, top - bottom
    )
    x = (A4_WIDTH - draw_w) / 2
    y = top - draw_h
    pdf.drawImage(image_path, x, y, width=draw_w, height=draw_h, preserveAspectRatio=True)
    return effective_dpi


def draw_stamp_header(pdf: canvas.Canvas, config: dict, problem_index: int, problem_total: int) -> None:
    x = PAGE_MARGIN
    y = 806
    height = 27
    label_width = 44
    total_width = A4_WIDTH - PAGE_MARGIN * 2
    radius = 5
    pdf.setStrokeColor(HexColor("#202020"))
    pdf.setLineWidth(1)
    pdf.roundRect(x, y, total_width, height, radius, fill=0, stroke=1)
    pdf.saveState()
    clip = pdf.beginPath()
    clip.roundRect(x, y, total_width, height, radius)
    pdf.clipPath(clip, stroke=0, fill=0)
    pdf.setFillColor(HexColor("#202020"))
    pdf.rect(x, y, label_width, height, fill=1, stroke=0)
    pdf.restoreState()
    pdf.setFillColor(white)
    pdf.setFont("BIZUDB", 12)
    grade_label = f"中{config.get('grade', 1)}"
    pdf.drawCentredString(x + label_width / 2, y + 8, grade_label)
    pdf.setFillColor(HexColor("#171717"))
    font_size = 10.5
    pdf.setFont("BIZUDB", font_size)
    stamp_text = config["stamp"]
    while pdf.stringWidth(stamp_text, "BIZUDB", font_size) > total_width - label_width - 16:
        font_size -= 0.25
        pdf.setFont("BIZUDB", font_size)
    pdf.drawString(x + label_width + 9, y + 8, stamp_text)
    pdf.setFont("BIZUD", 7)
    pdf.drawString(PAGE_MARGIN, 795, source_line(config))
    pdf.drawRightString(
        A4_WIDTH - PAGE_MARGIN, 795, f"問題 {problem_index} / {problem_total}"
    )
    draw_rule(pdf, 790)


def draw_problem_pages(
    pdf: canvas.Canvas,
    config: dict,
    rendered: dict,
    page_number: int,
    total_pages: int,
    metrics: list[dict],
) -> int:
    problem_pages = rendered["problem_flow"]
    problem_total = len(problem_pages)
    for index, slices in enumerate(problem_pages, 1):
        if index == 1:
            draw_stamp_header(pdf, config, index, problem_total)
            top = 782
        else:
            draw_standard_header(pdf, f"問題　{index} / {problem_total}", config)
            top = CONTENT_TOP
        y = top
        for slice_number, item in enumerate(slices, 1):
            y -= item["gap_before"]
            px_w, px_h = item["pixels"]
            draw_w = item["draw_width"]
            draw_h = px_h / px_w * draw_w
            y -= draw_h
            x = (A4_WIDTH - draw_w) / 2
            pdf.drawImage(
                item["path"], x, y, width=draw_w, height=draw_h, preserveAspectRatio=True
            )
            effective_dpi = min(px_w / (draw_w / 72), px_h / (draw_h / 72))
            metrics.append(
                {
                    "section": "problem",
                    "index": index,
                    "slice": slice_number,
                    "effective_dpi": round(effective_dpi),
                }
            )
        if y < CONTENT_BOTTOM - 0.5:
            raise RuntimeError(
                f"Problem flow overflow for {config['slug']} page {index}: y={y:.2f}"
            )
        draw_footer(pdf, page_number, total_pages)
        pdf.showPage()
        page_number += 1
    return page_number


def answer_physical_size(config: dict, item: dict) -> tuple[float, float, float]:
    rotation = item["rotation"]
    if rotation in ("cw", "ccw"):
        page_w, page_h = SOURCE_PAGE_PT[1], SOURCE_PAGE_PT[0]
        ref_w, ref_h = tuple(item.get("upright_ref_size", (1518, 1075)))
    else:
        page_w, page_h = SOURCE_PAGE_PT
        ref_w, ref_h = tuple(item.get("upright_ref_size", (1075, 1518)))
    requested = item["requested_box"]
    box_w = requested[2] - requested[0]
    box_h = requested[3] - requested[1]
    scale = config["answer_scale"]
    target_w = box_w / ref_w * page_w * scale
    target_h = box_h / ref_h * page_h * scale
    return target_w, target_h, scale


def draw_answer_sheet_page(
    pdf: canvas.Canvas,
    config: dict,
    rendered: dict,
    page_number: int,
    total_pages: int,
    metrics: list[dict],
) -> int:
    is_landscape = bool(config.get("answer_page_landscape", False))
    page_width, page_height = landscape(A4) if is_landscape else A4
    pdf.setPageSize((page_width, page_height))
    draw_standard_header(pdf, "解答用紙", config, page_width, page_height)
    items = rendered["answer_sheet"]
    sizes = [answer_physical_size(config, item) for item in items]
    gap = 22
    total_height = sum(size[1] for size in sizes) + gap * (len(sizes) - 1)
    max_width = max(size[0] for size in sizes)
    content_top = page_height - 72 if is_landscape else 730
    content_bottom = 50 if is_landscape else 80
    available_height = content_top - content_bottom
    available_width = page_width - PAGE_MARGIN * 2
    # Narrow answer rows can be physically correct yet unusably small on A4.
    # Expand them to a practical worksheet width while preserving already-large
    # answer sheets. Per-question overrides remain available for unusual forms.
    target_width_ratio = config.get("answer_fit_width_ratio", 0.86)
    if target_width_ratio is None:
        minimum_width_ratio = float(config.get("answer_min_width_ratio", 0.72))
        minimum_expansion = max(1.0, available_width * minimum_width_ratio / max_width)
        fit_factor = min(minimum_expansion, available_width / max_width, available_height / total_height)
    else:
        requested_width = available_width * float(target_width_ratio)
        fit_factor = min(requested_width / max_width, available_height / total_height)
    draw_heights = [size[1] * fit_factor for size in sizes]
    draw_widths = [size[0] * fit_factor for size in sizes]
    group_height = sum(draw_heights) + gap * (len(items) - 1)
    # Keep the selected answer field directly below the header.  Vertically
    # centering a short row created a large blank band above it and made a
    # correct crop look like the lower edge of the source page had survived.
    # A top-aligned field is easier to verify and use when printed.
    y = content_top
    for index, (item, draw_w, draw_h) in enumerate(
        zip(items, draw_widths, draw_heights), 1
    ):
        y -= draw_h
        x = (page_width - draw_w) / 2
        pdf.drawImage(item["path"], x, y, width=draw_w, height=draw_h, preserveAspectRatio=True)
        px_w, px_h = item["pixels"]
        effective_dpi = min(px_w / (draw_w / 72), px_h / (draw_h / 72))
        metrics.append(
            {
                "section": "answer_sheet",
                "index": index,
                "effective_dpi": round(effective_dpi),
                "fit_factor": round(fit_factor, 3),
            }
        )
        y -= gap
    pdf.setFillColor(HexColor("#333333"))
    pdf.setFont("BIZUD", 7.5)
    label = config["answer_scale_label"]
    if fit_factor < 0.999:
        label += f"／A4収容のため{fit_factor * 100:.0f}%縮小"
    elif fit_factor > 1.001:
        label += f"／記入しやすい幅に{fit_factor * 100:.0f}%拡大"
    label_y = 29 if is_landscape else 58
    footer_y = 10 if is_landscape else 17
    pdf.drawCentredString(page_width / 2, label_y, label)
    draw_footer(pdf, page_number, total_pages, page_width, footer_y)
    pdf.showPage()
    if is_landscape:
        pdf.setPageSize(A4)
    return page_number + 1


def draw_raster_section(
    pdf: canvas.Canvas,
    config: dict,
    pages: list[list[dict]],
    title: str,
    section_name: str,
    page_number: int,
    total_pages: int,
    metrics: list[dict],
) -> int:
    count = len(pages)
    for index, items in enumerate(pages, 1):
        heading = title if count == 1 else f"{title}　{index} / {count}"
        draw_standard_header(pdf, heading, config)
        y = CONTENT_TOP
        for item_number, item in enumerate(items, 1):
            if item_number > 1:
                y -= PROBLEM_GAP
            px_w, px_h = item["pixels"]
            requested_width = item["draw_width"]
            requested_height = px_h / px_w * requested_width
            if requested_height > y - CONTENT_BOTTOM:
                fit_factor = (y - CONTENT_BOTTOM) / requested_height
                draw_w = requested_width * fit_factor
                draw_h = requested_height * fit_factor
            else:
                draw_w = requested_width
                draw_h = requested_height
            y -= draw_h
            x = (A4_WIDTH - draw_w) / 2
            pdf.drawImage(
                item["path"], x, y, width=draw_w, height=draw_h, preserveAspectRatio=True
            )
            effective_dpi = min(px_w / (draw_w / 72), px_h / (draw_h / 72))
            metrics.append(
                {
                    "section": section_name,
                    "index": index,
                    "item": item_number,
                    "effective_dpi": round(effective_dpi),
                }
            )
        draw_footer(pdf, page_number, total_pages)
        pdf.showPage()
        page_number += 1
    return page_number


def build_pdf(config: dict, rendered: dict) -> dict:
    STAGING.mkdir(parents=True, exist_ok=True)
    output_path = STAGING / config["filename"]
    total_pages = (
        len(rendered["problem_flow"])
        + 1
        + len(rendered["answers_flow"])
        + len(rendered["explanation_flow"])
    )
    title = output_path.stem
    pdf = canvas.Canvas(str(output_path), pagesize=A4, pageCompression=1)
    pdf.setTitle(title)
    pdf.setAuthor("高校入試問題抜粋プロジェクト")
    pdf.setSubject(config["stamp"])
    metrics: list[dict] = []
    page_number = 1
    page_number = draw_problem_pages(
        pdf, config, rendered, page_number, total_pages, metrics
    )
    page_number = draw_answer_sheet_page(
        pdf, config, rendered, page_number, total_pages, metrics
    )
    page_number = draw_raster_section(
        pdf,
        config,
        rendered["answers_flow"],
        "正解（全問）",
        "answers",
        page_number,
        total_pages,
        metrics,
    )
    page_number = draw_raster_section(
        pdf,
        config,
        rendered["explanation_flow"],
        f"解説（大問{config['question']}）",
        "explanation",
        page_number,
        total_pages,
        metrics,
    )
    pdf.save()

    reader = PdfReader(str(output_path))
    if len(reader.pages) != total_pages:
        raise RuntimeError(f"Page count mismatch for {output_path}")
    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        portrait_a4 = abs(width - A4_WIDTH) <= 0.2 and abs(height - A4_HEIGHT) <= 0.2
        landscape_a4 = abs(width - A4_HEIGHT) <= 0.2 and abs(height - A4_WIDTH) <= 0.2
        if not (portrait_a4 or landscape_a4):
            raise RuntimeError(f"Non-A4 page in {output_path}: {width} x {height}")
    minimum_dpi = min(item["effective_dpi"] for item in metrics)
    return {
        "output": str(output_path),
        "final_output": str(PUBLISH / config["filename"]),
        "pages": total_pages,
        "bytes": output_path.stat().st_size,
        "minimum_effective_dpi": minimum_dpi,
        "metrics": metrics,
    }


def main() -> None:
    ensure_tools()
    register_fonts()
    if WORK.exists():
        # Windowsでは画像プレビュー中の一時PNGがロックされることがあるため、
        # 完全削除に失敗しても再生成を継続できるようにする。
        for attempt in range(3):
            try:
                shutil.rmtree(WORK)
                break
            except PermissionError:
                if attempt == 2:
                    break
                time.sleep(0.4)
    CROPS.mkdir(parents=True, exist_ok=True)
    selected_slugs = set(sys.argv[1:])
    selected = [
        config for config in CONFIGS if not selected_slugs or config["slug"] in selected_slugs
    ]
    if selected_slugs and len(selected) != len(selected_slugs):
        known = {config["slug"] for config in CONFIGS}
        raise ValueError(f"Unknown slugs: {sorted(selected_slugs - known)}")
    reports = []
    for index, config in enumerate(selected, 1):
        print(f"[{index}/{len(selected)}] rendering {config['slug']}", flush=True)
        rendered = render_config(config)
        prepare_problem_flow(config, rendered)
        rendered["answers_flow"] = prepare_raster_flow(rendered["answers"])
        rendered["explanation_flow"] = prepare_raster_flow(rendered["explanation"])
        print(f"[{index}/{len(selected)}] building {config['filename']}", flush=True)
        report = build_pdf(config, rendered)
        final_path = Path(report["final_output"])
        continuous_path = CONTINUOUS / config["filename"]
        final_path.parent.mkdir(parents=True, exist_ok=True)
        continuous_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copyfile(report["output"], final_path)
            shutil.copyfile(report["output"], continuous_path)
            report["published"] = True
            report["continuous_output"] = str(continuous_path)
        except PermissionError:
            report["published"] = False
            print(f"[{index}/{len(selected)}] final file is open; staged copy retained", flush=True)
        reports.append(report)
        print(
            f"[{index}/{len(selected)}] done: {report['pages']} pages, "
            f"min {report['minimum_effective_dpi']} dpi",
            flush=True,
        )
    report_path = WORK / "build-report.json"
    report_path.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(report_path), flush=True)


if __name__ == "__main__":
    main()
