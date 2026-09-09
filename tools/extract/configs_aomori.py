"""青森県・数学 採用4題の150dpi基準切り出し設定。

原本は ``D:\\Files\\(高校入試)青森県`` に保存されている。
2019年は問題、解答用紙、正解・解説が別PDF、2020年以降は問題と
正解・解説が年度別の ``{year}_数学.pdf`` にまとまっている。

採用対象は2019・2020・2021・2023年の大問5。問題文、全設問、解説の
途中式まで中学1・2年範囲であることを目視確認した。座標はすべて原本を
150dpiで描画して確認し、ページごとの画像寸法差を各 ``ref_size`` に保持する。
"""

from __future__ import annotations

from pathlib import Path


SOURCE_ROOT = Path(r"D:\Files\(高校入試)青森県")


def box(x1: int, y1: int, x2: int, y2: int) -> list[int]:
    return [x1, y1, x2, y2]


def fragment(
    page: int,
    bounds: tuple[int, int, int, int],
    ref_size: tuple[int, int],
) -> dict:
    return {
        "page": page,
        "box": box(*bounds),
        "ref_size": list(ref_size),
    }


def answer_fragment(bounds: tuple[int, int, int, int]) -> dict:
    return {
        "page": 1,
        "box": box(*bounds),
        "source_ref_size": [1075, 1518],
        "rotation": 0,
    }


SOURCES = {
    2019: {
        "problem_source_pdf": str((SOURCE_ROOT / "Z02_2019_M.pdf").resolve()),
        "answer_source_pdf": str(
            (SOURCE_ROOT / "Z02_2019_解答用紙.pdf").resolve()
        ),
        "answers_source_pdf": str((SOURCE_ROOT / "Z02_2019_KK.pdf").resolve()),
        "explanation_source_pdf": str(
            (SOURCE_ROOT / "Z02_2019_KK.pdf").resolve()
        ),
    },
    **{
        year: {
            "problem_source_pdf": str(
                (SOURCE_ROOT / f"{year}_数学.pdf").resolve()
            ),
            "answer_source_pdf": str(
                (SOURCE_ROOT / f"Z02_{year}_解答用紙.pdf").resolve()
            ),
            "answers_source_pdf": str(
                (SOURCE_ROOT / f"{year}_数学.pdf").resolve()
            ),
            "explanation_source_pdf": str(
                (SOURCE_ROOT / f"{year}_数学.pdf").resolve()
            ),
        }
        for year in (2020, 2021, 2023)
    },
}


SCIENCE_REFS = {
    2019: [1264, 1707],
    2020: [1018, 1525],
    2021: [1018, 1524],
    2023: [1020, 1527],
}


ANSWER_SCALES = {
    2019: 1.64,
    2020: 1.59,
    2021: 1.61,
    2023: 1.92,
}


WHOLE_ANSWERS = {
    2019: [fragment(1, (200, 430, 1065, 1100), (1264, 1707))],
    2020: [fragment(6, (65, 360, 930, 890), (1018, 1523))],
    2021: [fragment(6, (65, 365, 920, 925), (1018, 1524))],
    2023: [fragment(7, (65, 360, 930, 900), (1019, 1526))],
}


def config(
    *,
    year: int,
    grade: int,
    field: str,
    detail_unit: str,
    filename_unit: str,
    stamp: str,
    problem: list[dict],
    answer_sheet: list[dict],
    explanation: list[dict],
    problem_page_groups: list[list[int]] | None = None,
) -> dict:
    scale = ANSWER_SCALES[year]
    result = {
        "slug": f"aomori_q5_{year}_math",
        "year": year,
        "grade": grade,
        "prefecture": "青森県",
        "question": 5,
        "question_label": "大問5",
        "field": field,
        "detail_unit": detail_unit,
        "filename": f"{year}年実施_青森県_中{grade}数学_{filename_unit}.pdf",
        "stamp": stamp,
        "science_ref": SCIENCE_REFS[year],
        **SOURCES[year],
        "problem": problem,
        "answer_scale": scale,
        "answer_scale_label": (
            f"原本指定の{round(scale * 100)}%で配置（該当大問の解答欄のみ）"
        ),
        "answer_sheet": answer_sheet,
        "answers": WHOLE_ANSWERS[year],
        "explanation": explanation,
    }
    if problem_page_groups is not None:
        result["problem_page_groups"] = problem_page_groups
    return result


CONFIGS = [
    # 2019年：問題は全教科合本p5-6、正解p1、解説p4、解答用紙p1。
    config(
        year=2019,
        grade=2,
        field="規則性",
        detail_unit="規則性（卒業文集のページ配置・文字式）",
        filename_unit="規則性（卒業文集のページ配置・文字式）",
        stamp="規則性 - 卒業文集のページ配置、文字式",
        problem=[
            fragment(5, (200, 810, 1065, 1490), (1264, 1707)),
            fragment(6, (200, 230, 1065, 1085), (1264, 1707)),
        ],
        answer_sheet=[answer_fragment((160, 1275, 910, 1385))],
        explanation=[fragment(4, (200, 440, 1065, 1060), (1264, 1707))],
        problem_page_groups=[[1], [2]],
    ),
    # 2020年：問題p4-5、正解p6、解説p8-9、解答用紙p1。
    config(
        year=2020,
        grade=2,
        field="関数",
        detail_unit="一次関数とグラフの利用（水そうへの注水・水面の高さ）",
        filename_unit="一次関数とグラフの利用（水そうへの注水・水面の高さ）",
        stamp="一次関数とグラフの利用 - 水そうへの注水、水面の高さ",
        problem=[
            fragment(4, (75, 875, 950, 1420), (1018, 1525)),
            fragment(5, (95, 150, 925, 1050), (1016, 1526)),
        ],
        answer_sheet=[answer_fragment((150, 978, 865, 1375))],
        explanation=[
            fragment(8, (65, 1210, 950, 1438), (1017, 1524)),
            fragment(9, (95, 170, 950, 660), (1017, 1526)),
        ],
        problem_page_groups=[[1], [2]],
    ),
    # 2021年：大問5の導入は問題p4下、グラフと全設問はp5。
    # 正解p6、解説p9-10、解答用紙p1。
    config(
        year=2021,
        grade=2,
        field="関数",
        detail_unit="一次関数とグラフの利用（徒歩・バス・2人の距離）",
        filename_unit="一次関数とグラフの利用（徒歩・バス・2人の距離）",
        stamp="一次関数とグラフの利用 - 徒歩、バス、2人の距離",
        problem=[
            fragment(4, (75, 1165, 940, 1395), (1018, 1524)),
            fragment(5, (110, 155, 950, 1210), (1017, 1526)),
        ],
        answer_sheet=[answer_fragment((160, 925, 925, 1395))],
        explanation=[
            fragment(9, (95, 930, 950, 1425), (1016, 1524)),
            fragment(10, (95, 170, 950, 540), (1018, 1523)),
        ],
        problem_page_groups=[[1, 2]],
    ),
    # 2023年：問題p5-6、正解p7、解説p10、解答用紙p1。
    config(
        year=2023,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（りんごとなし・整数解・一次関数）",
        filename_unit="連立方程式の利用（りんごとなし・整数解・一次関数）",
        stamp="連立方程式の利用 - りんごとなし、整数解、一次関数",
        problem=[
            fragment(5, (105, 585, 935, 1330), (1020, 1527)),
            fragment(6, (105, 155, 915, 715), (1021, 1528)),
        ],
        answer_sheet=[answer_fragment((540, 845, 865, 1240))],
        explanation=[fragment(10, (95, 395, 950, 910), (1022, 1526))],
        problem_page_groups=[[1], [2]],
    ),
]
