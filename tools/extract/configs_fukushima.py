"""福島県2020〜2025年・採用10題の150dpi基準切り出し設定。

原本は ``D:\\Files\\(高校入試)福島県_2025`` に保存されている。
各年度の数学PDFには問題・正解一覧・解説が収録され、解答用紙は
年度別の別PDFに収録されている。

問題文、全設問、解説途中式を全ページ画像で確認し、中学1・2年範囲だけで
完結する独立大問を採用した。小問集合、学校裁量問題、中学3年内容を含む
大問は除外している。座標は原本を150dpiで描画した実寸を基準とする。
"""

from __future__ import annotations

from pathlib import Path


SOURCE_ROOT = Path(r"D:\Files\(高校入試)福島県_2025")


PAGE_REFS = {
    2020: {page: [1075, 1518] for page in range(1, 11)},
    2021: {
        1: [1024, 1526],
        2: [1018, 1523],
        3: [1021, 1523],
        4: [1018, 1525],
        5: [1021, 1523],
        6: [1017, 1521],
        7: [1016, 1524],
        8: [1017, 1523],
        9: [1016, 1522],
    },
    2022: {
        1: [1016, 1524],
        2: [1015, 1525],
        3: [1014, 1525],
        4: [1023, 1523],
        5: [1013, 1525],
        6: [1015, 1524],
        7: [1015, 1527],
        8: [1020, 1524],
        9: [1016, 1526],
    },
    2023: {
        1: [1012, 1525],
        2: [1012, 1524],
        3: [1012, 1526],
        4: [1016, 1525],
        5: [1012, 1524],
        6: [1014, 1523],
        7: [1014, 1524],
        8: [1015, 1523],
        9: [1015, 1526],
    },
    2024: {
        1: [1011, 1524],
        2: [1011, 1524],
        3: [1013, 1524],
        4: [1012, 1523],
        5: [1013, 1524],
        6: [1011, 1523],
        7: [1014, 1523],
        8: [1012, 1522],
        9: [1011, 1524],
    },
    2025: {
        1: [1012, 1524],
        2: [1012, 1525],
        3: [1012, 1526],
        4: [1011, 1523],
        5: [1012, 1525],
        6: [1012, 1524],
        7: [1012, 1524],
        8: [1014, 1524],
        9: [1012, 1525],
    },
}


SOURCES = {
    year: {
        "problem_source_pdf": str(
            (SOURCE_ROOT / f"{year}_福島県_数学.pdf").resolve()
        ),
        "answer_source_pdf": str(
            (SOURCE_ROOT / f"{year}_福島県{year}解答用紙.pdf").resolve()
        ),
        "answers_source_pdf": str(
            (SOURCE_ROOT / f"{year}_福島県_数学.pdf").resolve()
        ),
        "explanation_source_pdf": str(
            (SOURCE_ROOT / f"{year}_福島県_数学.pdf").resolve()
        ),
    }
    for year in range(2020, 2026)
}


ANSWER_SCALES = {
    2020: (2.00, "原本指定の200%で配置（解答欄は実物大相当）"),
    2021: (2.00, "原本指定の200%で配置（解答欄は実物大相当）"),
    2022: (1.92, "原本指定の192%で配置（解答欄は実物大相当）"),
    2023: (1.00, "原本に拡大率指定なし（100%で配置）"),
    2024: (1.92, "原本指定の192%で配置（解答欄は実物大相当）"),
    2025: (1.00, "原本に拡大率指定なし（100%で配置）"),
}


WHOLE_ANSWERS = {
    2020: [(7, [105, 350, 970, 770])],
    2021: [(6, [55, 355, 920, 800])],
    2022: [(6, [55, 360, 915, 675])],
    2023: [(6, [50, 360, 915, 760])],
    2024: [(7, [55, 355, 920, 750])],
    2025: [(6, [55, 365, 920, 695])],
}


def piece(year: int, page: int, bounds: list[int]) -> dict:
    return {
        "page": page,
        "box": bounds,
        "ref_size": PAGE_REFS[year][page],
    }


def pieces(year: int, items: list[tuple[int, list[int]]]) -> list[dict]:
    return [piece(year, page, bounds) for page, bounds in items]


def config(
    *,
    year: int,
    question: int,
    field: str,
    detail_unit: str,
    stamp: str,
    problem: list[tuple[int, list[int]]],
    answer_box: list[int],
    explanation: list[tuple[int, list[int]]],
    problem_page_groups: list[list[int]] | None = None,
) -> dict:
    answer_scale, answer_scale_label = ANSWER_SCALES[year]
    result = {
        "slug": f"fukushima_q{question}_{year}",
        "repo": "local-source-fukushima",
        "year": year,
        "prefecture": "福島県",
        "question": question,
        "question_label": f"大問{question}",
        "grade": 2,
        "field": field,
        "detail_unit": detail_unit,
        "filename": f"{year}年実施_福島県_中2数学_{detail_unit}.pdf",
        "stamp": stamp,
        "science_ref": PAGE_REFS[year][problem[0][0]],
        **SOURCES[year],
        "problem": pieces(year, problem),
        "answer_scale": answer_scale,
        "answer_scale_label": answer_scale_label,
        "answer_sheet": [
            {
                "page": 1,
                "box": answer_box,
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            }
        ],
        "answers": pieces(year, WHOLE_ANSWERS[year]),
        "explanation": pieces(year, explanation),
    }
    if problem_page_groups is not None:
        result["problem_page_groups"] = problem_page_groups
    return result


CONFIGS = [
    config(
        year=2020,
        question=4,
        field="方程式の利用",
        detail_unit="連立方程式の利用（硬貨の枚数・貯金額・一次関数）",
        stamp="連立方程式の利用 - 硬貨の枚数、貯金額、一次関数",
        problem=[(3, [100, 390, 970, 1335])],
        answer_box=[555, 260, 965, 610],
        explanation=[
            (8, [95, 1375, 965, 1445]),
            (9, [120, 155, 980, 470]),
        ],
    ),
    config(
        year=2021,
        question=4,
        field="方程式の利用",
        detail_unit="連立方程式の利用（3けたの自然数・各位の数字・数字の入れかえ）",
        stamp="連立方程式の利用 - 3けたの自然数、各位の数字、数字の入れかえ",
        problem=[(3, [70, 595, 930, 790])],
        answer_box=[545, 270, 940, 625],
        explanation=[(7, [65, 1135, 970, 1410])],
    ),
    config(
        year=2021,
        question=5,
        field="図形の証明",
        detail_unit="三角形の合同証明（合同な三角形・角の差・線分の差）",
        stamp="三角形の合同証明 - 合同な三角形、角の差、線分の差",
        problem=[(3, [70, 795, 930, 1470])],
        answer_box=[545, 635, 940, 1045],
        explanation=[(8, [65, 165, 945, 455])],
    ),
    config(
        year=2022,
        question=4,
        field="方程式の利用",
        detail_unit="連立方程式の利用（じゃんけん・勝敗回数・メダルの重さ）",
        stamp="連立方程式の利用 - じゃんけん、勝敗回数、メダルの重さ",
        problem=[(3, [90, 480, 960, 950])],
        answer_box=[500, 250, 970, 625],
        explanation=[(7, [65, 1110, 970, 1340])],
    ),
    config(
        year=2022,
        question=5,
        field="図形の証明",
        detail_unit="三角形の合同証明（角の二等分線・平行線・平行四辺形）",
        stamp="三角形の合同証明 - 角の二等分線、平行線、平行四辺形",
        problem=[(3, [90, 970, 945, 1415])],
        answer_box=[500, 635, 970, 1045],
        explanation=[
            (7, [65, 1355, 970, 1475]),
            (8, [65, 160, 950, 455]),
        ],
    ),
    config(
        year=2023,
        question=4,
        field="方程式の利用",
        detail_unit="連立方程式の利用（グループ分け・人数・予備のごみ袋）",
        stamp="連立方程式の利用 - グループ分け、人数、予備のごみ袋",
        problem=[(3, [100, 395, 960, 595])],
        answer_box=[495, 245, 970, 625],
        explanation=[(7, [65, 1130, 970, 1345])],
    ),
    config(
        year=2024,
        question=4,
        field="方程式の利用",
        detail_unit="連立方程式の利用（水の移動・分数の割合）",
        stamp="連立方程式の利用 - 水の移動、分数の割合",
        problem=[(3, [100, 708, 960, 900])],
        answer_box=[495, 250, 970, 615],
        explanation=[(8, [65, 1015, 960, 1270])],
    ),
    config(
        year=2024,
        question=5,
        field="図形の証明",
        detail_unit="三角形の合同証明（合同な長方形・回転・直角三角形）",
        stamp="三角形の合同証明 - 合同な長方形、回転、直角三角形",
        problem=[
            (3, [100, 915, 980, 1410]),
            (4, [65, 140, 945, 905]),
        ],
        answer_box=[495, 625, 970, 1090],
        explanation=[
            (8, [65, 1285, 960, 1475]),
            (9, [65, 160, 950, 380]),
        ],
        problem_page_groups=[[1], [2]],
    ),
    config(
        year=2025,
        question=4,
        field="方程式の利用",
        detail_unit="連立方程式の利用（高速道路と一般道・時間と道のり）",
        stamp="連立方程式の利用 - 高速道路と一般道、時間と道のり",
        problem=[(3, [95, 485, 950, 815])],
        answer_box=[500, 250, 970, 615],
        explanation=[
            (7, [65, 1350, 970, 1475]),
            (8, [65, 160, 950, 270]),
        ],
    ),
    config(
        year=2025,
        question=5,
        field="図形の証明",
        detail_unit="三角形の合同証明（平行四辺形・証明の穴埋めと完成）",
        stamp="三角形の合同証明 - 平行四辺形、証明の穴埋めと完成",
        problem=[
            (3, [95, 835, 950, 1415]),
            (4, [65, 140, 945, 470]),
        ],
        answer_box=[500, 625, 970, 1085],
        explanation=[(8, [65, 285, 950, 780])],
        problem_page_groups=[[1], [2]],
    ),
]
