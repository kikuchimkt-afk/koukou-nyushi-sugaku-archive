"""数学大問の切り出し設定を、PDF生成前に機械検査する。"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from pypdf import PdfReader

from configs import CONFIGS


REPO = Path(__file__).resolve().parents[2]
GITHUB = REPO.parent
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
EXPECTED_BY_PREFECTURE = {"北海道": 8, "福岡県": 11, "長野県": 3}
EXPECTED_BY_GRADE_FIELD = {
    (1, "データの活用"): 4,
    (2, "数と式"): 1,
    (2, "方程式の利用"): 1,
    (2, "規則性"): 3,
    (2, "関数"): 8,
    (2, "図形の証明"): 2,
    (2, "データの活用"): 3,
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
REQUIRED_KEYS = {
    "slug",
    "repo",
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


def main() -> None:
    if len(CONFIGS) != 22:
        raise ValueError(f"Expected 22 configs, got {len(CONFIGS)}")
    slugs = [config["slug"] for config in CONFIGS]
    filenames = [config["filename"] for config in CONFIGS]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate slug")
    if len(filenames) != len(set(filenames)):
        raise ValueError("Duplicate filename")

    actual_selection = {
        (
            config["slug"],
            config["repo"],
            config["year"],
            config["prefecture"],
            config["question"],
            config["grade"],
            config["field"],
            config["filename"],
        )
        for config in CONFIGS
    }
    if actual_selection != EXPECTED_SELECTION:
        missing = sorted(EXPECTED_SELECTION - actual_selection)
        extra = sorted(actual_selection - EXPECTED_SELECTION)
        raise ValueError(f"Approved selection differs: missing={missing} extra={extra}")

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

        base = GITHUB / config["repo"] / "public" / "files" / str(config["year"])
        problem_pdf = base / "解説付き問題" / "数学.pdf"
        answer_pdf = base / "解答用紙" / "数学.pdf"
        if not problem_pdf.is_file() or not answer_pdf.is_file():
            raise FileNotFoundError(f"{slug}: source PDF missing")
        problem_pages = len(PdfReader(problem_pdf).pages)
        answer_pages = len(PdfReader(answer_pdf).pages)

        for section in ("problem", "answers", "explanation"):
            if not config[section]:
                raise ValueError(f"{slug}: empty {section}")
            for index, item in enumerate(config[section], 1):
                page = item.get("page")
                if not isinstance(page, int) or not 1 <= page <= problem_pages:
                    raise ValueError(f"{slug}/{section}/{index}: invalid page {page}")
                ref = tuple(item.get("ref_size", config["science_ref"]))
                validate_box(f"{slug}/{section}/{index}", item, ref)

        if not config["answer_sheet"]:
            raise ValueError(f"{slug}: empty answer_sheet")
        for index, item in enumerate(config["answer_sheet"], 1):
            page = item.get("page", 1)
            if not 1 <= page <= answer_pages:
                raise ValueError(f"{slug}/answer_sheet/{index}: invalid page {page}")
            source_ref = tuple(item.get("source_ref_size", item.get("ref_size", (1075, 1518))))
            rotation = item.get("rotation", 0)
            upright_ref = (source_ref[1], source_ref[0]) if rotation in ("cw", "ccw") else source_ref
            validate_box(f"{slug}/answer_sheet/{index}", item, upright_ref)

    by_prefecture = Counter(config["prefecture"] for config in CONFIGS)
    by_grade_field = Counter((config["grade"], config["field"]) for config in CONFIGS)
    if dict(by_prefecture) != EXPECTED_BY_PREFECTURE:
        raise ValueError(f"Prefecture counts differ: {dict(by_prefecture)}")
    if dict(by_grade_field) != EXPECTED_BY_GRADE_FIELD:
        raise ValueError(f"Grade/field counts differ: {dict(by_grade_field)}")
    print("OK: 22 configs / sources present / pages and boxes valid / counts match")


if __name__ == "__main__":
    main()
