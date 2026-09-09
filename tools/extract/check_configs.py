"""数学大問の切り出し設定を、PDF生成前に機械検査する。"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pypdf import PdfReader

from configs import CONFIGS
from source_paths import section_source_path, source_paths


FIELDS = {
    "数と式",
    "方程式",
    "方程式の利用",
    "規則性",
    "関数",
    "図形",
    "図形の証明",
    "データの活用",
}
EXPECTED_CONFIG_COUNT = 136
EXPECTED_BY_PREFECTURE = {
    "北海道": 8,
    "青森県": 4,
    "福岡県": 11,
    "長野県": 3,
    "群馬県": 20,
    "岐阜県": 14,
    "沖縄県": 27,
    "岩手県": 37,
    "徳島県": 12,
}
EXPECTED_BY_GRADE_FIELD = {
    (1, "数と式"): 4,
    (1, "方程式の利用"): 3,
    (1, "関数"): 7,
    (1, "図形"): 11,
    (1, "データの活用"): 12,
    (2, "数と式"): 4,
    (2, "方程式の利用"): 17,
    (2, "規則性"): 14,
    (2, "関数"): 28,
    (2, "図形"): 3,
    (2, "図形の証明"): 10,
    (2, "データの活用"): 23,
}
EXPECTED_SELECTION = {
    (
        "hokkaido_q3_2018_math", "koukou-nyushi-hokkaido", 2018, "北海道", 3, 1,
        "データの活用", "2018年実施_北海道_中1数学_度数分布表と代表値（相対度数・平均値・中央値・階級）.pdf",
    ),
    (
        "hokkaido_q3_2019_math", "koukou-nyushi-hokkaido", 2019, "北海道", 3, 2,
        "規則性", "2019年実施_北海道_中2数学_文字式による説明（ます目の和・単項式・方程式の応用）.pdf",
    ),
    (
        "hokkaido_q5_2019_math", "koukou-nyushi-hokkaido", 2019, "北海道", 5, 2,
        "図形の証明", "2019年実施_北海道_中2数学_台形と合同の証明（角度・垂線・三角形の合同）.pdf",
    ),
    (
        "hokkaido_q3_2020_math", "koukou-nyushi-hokkaido", 2020, "北海道", 3, 2,
        "規則性", "2020年実施_北海道_中2数学_整数の性質と文字式（倍数・カレンダー・うるう年の周期）.pdf",
    ),
    (
        "hokkaido_q3_2021_math", "koukou-nyushi-hokkaido", 2021, "北海道", 3, 2,
        "規則性", "2021年実施_北海道_中2数学_規則性と文字式（ストロー・五角形・正六角形・説明）.pdf",
    ),
    (
        "hokkaido_q5_2021_math", "koukou-nyushi-hokkaido", 2021, "北海道", 5, 2,
        "図形の証明", "2021年実施_北海道_中2数学_台形と合同の証明（対角線・平行線と角・線分の相等）.pdf",
    ),
    (
        "hokkaido_q2_2022_math", "koukou-nyushi-hokkaido", 2022, "北海道", 2, 2,
        "データの活用", "2022年実施_北海道_中2数学_箱ひげ図と四分位数（第3四分位数・範囲・中央値・分布）.pdf",
    ),
    (
        "hokkaido_q5_2023_math", "koukou-nyushi-hokkaido", 2023, "北海道", 5, 1,
        "データの活用", "2023年実施_北海道_中1数学_度数分布と相対度数（累積度数・度数折れ線・分布の比較）.pdf",
    ),
    (
        "fukuoka_q2_2017", "koukou-nyushi-fukuoka", 2017, "福岡県", 2, 2,
        "方程式の利用", "2017年実施_福岡県_中2数学_連立方程式の応用（袋詰めの個数と売上金額）.pdf",
    ),
    (
        "fukuoka_q4_2017", "koukou-nyushi-fukuoka", 2017, "福岡県", 4, 2,
        "関数", "2017年実施_福岡県_中2数学_一次関数のグラフの利用（速さ・道のり・すれちがい）.pdf",
    ),
    (
        "fukuoka_q3_2018", "koukou-nyushi-fukuoka", 2018, "福岡県", 3, 1,
        "データの活用", "2018年実施_福岡県_中1数学_相対度数と中央値（2校の読書冊数の比較）.pdf",
    ),
    (
        "fukuoka_q4_2018", "koukou-nyushi-fukuoka", 2018, "福岡県", 4, 2,
        "関数", "2018年実施_福岡県_中2数学_一次関数のグラフの利用（水そうの水面の高さ）.pdf",
    ),
    (
        "fukuoka_q2_2019", "koukou-nyushi-fukuoka", 2019, "福岡県", 2, 2,
        "データの活用", "2019年実施_福岡県_中2数学_確率（玉の取り出し・2種類のくじ引きの比較）.pdf",
    ),
    (
        "fukuoka_q3_2019", "koukou-nyushi-fukuoka", 2019, "福岡県", 3, 2,
        "数と式", "2019年実施_福岡県_中2数学_式の値と等式の変形（数当てゲームの仕組みの説明）.pdf",
    ),
    (
        "fukuoka_q4_2019", "koukou-nyushi-fukuoka", 2019, "福岡県", 4, 2,
        "関数", "2019年実施_福岡県_中2数学_一次関数のグラフの利用（通学の道のりと時間）.pdf",
    ),
    (
        "fukuoka_q3_2020", "koukou-nyushi-fukuoka", 2020, "福岡県", 3, 2,
        "データの活用", "2020年実施_福岡県_中2数学_場合の数と確率（カードとコマの移動）.pdf",
    ),
    (
        "fukuoka_q4_2020", "koukou-nyushi-fukuoka", 2020, "福岡県", 4, 2,
        "関数", "2020年実施_福岡県_中2数学_一次関数のグラフの利用（電話の料金プランの比較）.pdf",
    ),
    (
        "fukuoka_q2_2021", "koukou-nyushi-fukuoka", 2021, "福岡県", 2, 1,
        "データの活用", "2021年実施_福岡県_中1数学_相対度数と代表値（紙飛行機の飛行距離のヒストグラム）.pdf",
    ),
    (
        "fukuoka_q4_2021", "koukou-nyushi-fukuoka", 2021, "福岡県", 4, 2,
        "関数", "2021年実施_福岡県_中2数学_一次関数のグラフの利用（家・図書館・駅の移動）.pdf",
    ),
    (
        "nagano_2018_q3", "koukou-nyushi-nagano", 2018, "長野県", 3, 2,
        "関数", "2018年実施_長野県_中2数学_一次関数とダイヤグラム（2台のエレベーターの動き）.pdf",
    ),
    (
        "nagano_2019_q3", "koukou-nyushi-nagano", 2019, "長野県", 3, 2,
        "関数", "2019年実施_長野県_中2数学_一次関数のグラフの利用（プールの排水とポンプ）.pdf",
    ),
    (
        "nagano_2020_q3", "koukou-nyushi-nagano", 2020, "長野県", 3, 2,
        "関数", "2020年実施_長野県_中2数学_一次関数のグラフの読み取りと利用（2店のリボンの値段）.pdf",
    ),
}
EXPECTED_ADDITIONAL_SLUGS = {
    "aomori_q5_2019_math",
    "aomori_q5_2020_math",
    "aomori_q5_2021_math",
    "aomori_q5_2023_math",
    "gifu_q2_2018",
    "gifu_q2_2020",
    "gifu_q2_2021",
    "gifu_q3_2019",
    "gifu_q3_2021",
    "gifu_q3_2022",
    "gifu_q3_2023",
    "gifu_q4_2018",
    "gifu_q4_2019",
    "gifu_q4_2020",
    "gifu_q4_2021",
    "gifu_q4_2023",
    "gifu_q6_2019",
    "gifu_q6_2023",
    "gunma_2017_back_q4",
    "gunma_2017_front_q4",
    "gunma_2017_front_q5",
    "gunma_2018_back_q2",
    "gunma_2018_back_q3",
    "gunma_2018_back_q5",
    "gunma_2018_front_q4",
    "gunma_2018_front_q5",
    "gunma_2019_back_q2",
    "gunma_2019_back_q3",
    "gunma_2019_front_q4",
    "gunma_2020_back_q3",
    "gunma_2020_front_q3",
    "gunma_2021_back_q2",
    "gunma_2021_back_q3",
    "gunma_2021_back_q4",
    "gunma_2021_back_q5",
    "gunma_2021_front_q3",
    "gunma_2022_back_q4",
    "gunma_2022_back_q5",
    "iwate_q10_2021",
    "iwate_q10_2023",
    "iwate_q10_2024",
    "iwate_q10_2025",
    "iwate_q11_2022",
    "iwate_q2_2021",
    "iwate_q2_2022",
    "iwate_q2_2023",
    "iwate_q2_2024",
    "iwate_q2_2025",
    "iwate_q3_2021",
    "iwate_q3_2022",
    "iwate_q3_2023",
    "iwate_q3_2024",
    "iwate_q3_2025",
    "iwate_q5_2022",
    "iwate_q5_2023",
    "iwate_q5_2024",
    "iwate_q5_2025",
    "iwate_q6_2021",
    "iwate_q6_2022",
    "iwate_q6_2023",
    "iwate_q6_2024",
    "iwate_q6_2025",
    "iwate_q7_2021",
    "iwate_q7_2022",
    "iwate_q7_2023",
    "iwate_q7_2024",
    "iwate_q7_2025",
    "iwate_q8_2021",
    "iwate_q8_2022",
    "iwate_q8_2023",
    "iwate_q8_2024",
    "iwate_q8_2025",
    "iwate_q9_2021",
    "iwate_q9_2022",
    "iwate_q9_2025",
    "okinawa_q10_2019_math",
    "okinawa_q10_2020_math",
    "okinawa_q10_2021_math",
    "okinawa_q3_2019_math",
    "okinawa_q3_2020_math",
    "okinawa_q3_2021_math",
    "okinawa_q3_2022_math",
    "okinawa_q3_2023_math",
    "okinawa_q3_2024_math",
    "okinawa_q4_2019_math",
    "okinawa_q4_2020_math",
    "okinawa_q4_2021_math",
    "okinawa_q4_2022_math",
    "okinawa_q4_2023_math",
    "okinawa_q4_2024_math",
    "okinawa_q5_2019_math",
    "okinawa_q5_2020_math",
    "okinawa_q5_2021_math",
    "okinawa_q5_2023_math",
    "okinawa_q5_2024_math",
    "okinawa_q6_2019_math",
    "okinawa_q6_2020_math",
    "okinawa_q6_2022_math",
    "okinawa_q7_2023_math",
    "okinawa_q7_2024_math",
    "okinawa_q8_2020_math",
    "okinawa_q9_2022_math",
    "tokushima_2016_q2_math",
    "tokushima_2016_q5_math",
    "tokushima_2018_q5_math",
    "tokushima_2019_q3_math",
    "tokushima_2021_q2_math",
    "tokushima_2022_q3_math",
    "tokushima_2023_q3_math",
    "tokushima_2023_q4_math",
    "tokushima_2024_q3_math",
    "tokushima_2024_q4_math",
    "tokushima_2025_q2_math",
    "tokushima_2025_q3_math",
}
ADDITIONAL_SELECTION_KEYS = (
    "slug",
    "year",
    "prefecture",
    "session",
    "question",
    "grade",
    "field",
    "filename",
    "problem_source_pdf",
    "answer_source_pdf",
    "answers_source_pdf",
    "explanation_source_pdf",
)
EXPECTED_ADDITIONAL_SELECTION_SHA256 = (
    "6ab8cebf7169e890ffb4d3009e8f4f7f4aff9bb8a555b31de51757f0472fdd4a"
)
REQUIRED_KEYS = {
    "slug",
    "year",
    "prefecture",
    "question",
    "grade",
    "field",
    "filename",
    "stamp",
    "science_ref",
    "problem",
    "answer_scale",
    "answer_scale_label",
    "answer_sheet",
    "answers",
    "explanation",
}


def validate_box(label: str, item: dict, ref: tuple[int, int]) -> None:
    coords = item.get("box")
    if not isinstance(coords, list) or len(coords) != 4:
        raise ValueError(f"{label}: box must have four coordinates")
    x1, y1, x2, y2 = coords
    if not all(isinstance(value, int) for value in coords):
        raise ValueError(f"{label}: box coordinates must be integers")
    if not (0 <= x1 < x2 <= ref[0] and 0 <= y1 < y2 <= ref[1]):
        raise ValueError(f"{label}: box {coords} exceeds reference {ref}")


def validate_ref_size(
    label: str, ref: tuple[int, int], reader: PdfReader, page_number: int
) -> None:
    page = reader.pages[page_number - 1]
    expected_width = float(page.mediabox.width) * 150 / 72
    expected_height = float(page.mediabox.height) * 150 / 72
    if (page.rotation or 0) % 180:
        expected_width, expected_height = expected_height, expected_width
    expected = (round(expected_width), round(expected_height))
    if max(abs(ref[0] - expected[0]), abs(ref[1] - expected[1])) > 3:
        raise ValueError(
            f"{label}: ref_size {ref} differs from 150dpi page size {expected}"
        )


def additional_selection_sha256(configs: list[dict]) -> str:
    projection = [
        {key: config.get(key) for key in ADDITIONAL_SELECTION_KEYS}
        for config in configs
    ]
    payload = json.dumps(
        sorted(projection, key=lambda item: item["slug"]),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    if len(CONFIGS) != EXPECTED_CONFIG_COUNT:
        raise ValueError(
            f"Expected {EXPECTED_CONFIG_COUNT} configs, got {len(CONFIGS)}"
        )
    slugs = [config["slug"] for config in CONFIGS]
    filenames = [config["filename"] for config in CONFIGS]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate slug")
    if len(filenames) != len(set(filenames)):
        raise ValueError("Duplicate filename")

    actual_selection = {
        (
            config["slug"],
            config.get("repo") or config.get("problem_source_pdf"),
            config["year"],
            config["prefecture"],
            config["question"],
            config["grade"],
            config["field"],
            config["filename"],
        )
        for config in CONFIGS
    }
    existing_selection = {
        item for item in actual_selection if item[0] not in EXPECTED_ADDITIONAL_SLUGS
    }
    if existing_selection != EXPECTED_SELECTION:
        missing = sorted(EXPECTED_SELECTION - existing_selection)
        extra = sorted(existing_selection - EXPECTED_SELECTION)
        raise ValueError(f"Approved selection differs: missing={missing} extra={extra}")
    actual_additional_slugs = set(slugs) - {item[0] for item in EXPECTED_SELECTION}
    if actual_additional_slugs != EXPECTED_ADDITIONAL_SLUGS:
        missing = sorted(EXPECTED_ADDITIONAL_SLUGS - actual_additional_slugs)
        extra = sorted(actual_additional_slugs - EXPECTED_ADDITIONAL_SLUGS)
        raise ValueError(
            f"Additional approved selection differs: missing={missing} extra={extra}"
        )
    additional_configs = [
        config for config in CONFIGS if config["slug"] in EXPECTED_ADDITIONAL_SLUGS
    ]
    actual_selection_hash = additional_selection_sha256(additional_configs)
    if actual_selection_hash != EXPECTED_ADDITIONAL_SELECTION_SHA256:
        raise ValueError(
            "Additional approved selection metadata differs: "
            f"{actual_selection_hash} != {EXPECTED_ADDITIONAL_SELECTION_SHA256}"
        )

    for config in CONFIGS:
        missing = REQUIRED_KEYS - config.keys()
        if missing:
            raise ValueError(f"{config.get('slug', '(unknown)')}: missing {sorted(missing)}")
        slug = config["slug"]
        if config["field"] not in FIELDS:
            raise ValueError(f"{slug}: unknown field {config['field']}")
        expected_prefix = (
            f"{config['year']}年実施_{config['prefecture']}_中{config['grade']}数学_"
        )
        if not config["filename"].startswith(expected_prefix) or not config["filename"].endswith(".pdf"):
            raise ValueError(f"{slug}: invalid filename {config['filename']}")
        if not (0.5 <= float(config["answer_scale"]) <= 4.0):
            raise ValueError(f"{slug}: unreasonable answer scale")

        problem_pdf, answer_pdf = source_paths(config)
        answers_pdf = section_source_path(config, "answers", problem_pdf)
        explanation_pdf = section_source_path(config, "explanation", problem_pdf)
        section_readers = {
            "problem": PdfReader(problem_pdf),
            "answers": PdfReader(answers_pdf),
            "explanation": PdfReader(explanation_pdf),
        }
        section_page_counts = {
            section: len(reader.pages) for section, reader in section_readers.items()
        }
        answer_reader = PdfReader(answer_pdf)
        answer_pages = len(answer_reader.pages)

        for section in ("problem", "answers", "explanation"):
            if not config[section]:
                raise ValueError(f"{slug}: empty {section}")
            for index, item in enumerate(config[section], 1):
                page = item.get("page")
                if not isinstance(page, int) or not 1 <= page <= section_page_counts[section]:
                    raise ValueError(f"{slug}/{section}/{index}: invalid page {page}")
                default_ref = {
                    "problem": config["science_ref"],
                    "answers": config.get("answers_ref", config["science_ref"]),
                    "explanation": config.get(
                        "explanation_ref", config["science_ref"]
                    ),
                }[section]
                ref = tuple(item.get("ref_size", default_ref))
                validate_ref_size(
                    f"{slug}/{section}/{index}",
                    ref,
                    section_readers[section],
                    page,
                )
                validate_box(f"{slug}/{section}/{index}", item, ref)

        if not config["answer_sheet"]:
            raise ValueError(f"{slug}: empty answer_sheet")
        for index, item in enumerate(config["answer_sheet"], 1):
            page = item.get("page", 1)
            if not 1 <= page <= answer_pages:
                raise ValueError(f"{slug}/answer_sheet/{index}: invalid page {page}")
            source_ref = tuple(item.get("source_ref_size", item.get("ref_size", (1075, 1518))))
            validate_ref_size(
                f"{slug}/answer_sheet/{index}", source_ref, answer_reader, page
            )
            rotation = item.get("rotation", 0)
            upright_ref = (source_ref[1], source_ref[0]) if rotation in ("cw", "ccw") else source_ref
            validate_box(f"{slug}/answer_sheet/{index}", item, upright_ref)

    by_prefecture = Counter(config["prefecture"] for config in CONFIGS)
    by_grade_field = Counter((config["grade"], config["field"]) for config in CONFIGS)
    if dict(by_prefecture) != EXPECTED_BY_PREFECTURE:
        raise ValueError(f"Prefecture counts differ: {dict(by_prefecture)}")
    if dict(by_grade_field) != EXPECTED_BY_GRADE_FIELD:
        raise ValueError(f"Grade/field counts differ: {dict(by_grade_field)}")
    print(
        f"OK: {len(CONFIGS)} configs / sources present / "
        "pages and boxes valid / counts match"
    )


if __name__ == "__main__":
    main()
