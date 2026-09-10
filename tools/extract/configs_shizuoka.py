"""静岡県 2019〜2024年・採用12題の150dpi基準切り出し設定。

原本は ``D:\\Files\\(高校入試)静岡県`` に保存された一般選抜の数学問題、
解答用紙、正解・解説である。問題文と解説過程を全ページ目視し、中学1・2年
範囲だけで完結する独立大問を採用した。大問1・2の小問集合、および空間図形、
二次関数、相似・円など中学3年内容を含む大問は除外している。

2019年は問題、解答用紙、正解・解説が別PDF、2020年以降は年度別数学PDFに
問題と正解・解説がまとまっている。ページごとの画像寸法差を吸収するため、
全断片に150dpiで実測した ``ref_size`` を付ける。
"""

from __future__ import annotations


_ROOT = r"D:\Files\(高校入試)静岡県"

_SOURCES = {
    2019: {
        "problem_source_pdf": _ROOT + r"\Z22_2019_M.pdf",
        "answer_source_pdf": _ROOT + r"\Z22_2019_Y.pdf",
        "answers_source_pdf": _ROOT + r"\Z22_2019_KK.pdf",
        "explanation_source_pdf": _ROOT + r"\Z22_2019_KK.pdf",
    },
    **{
        year: {
            "problem_source_pdf": _ROOT + rf"\{year}_数学.pdf",
            "answer_source_pdf": _ROOT + rf"\Z22_{year}_解答用紙.pdf",
            "answers_source_pdf": _ROOT + rf"\{year}_数学.pdf",
            "explanation_source_pdf": _ROOT + rf"\{year}_数学.pdf",
        }
        for year in range(2020, 2025)
    },
}

# pdftoppm -r 150 でレンダリングした、使用ページごとの実寸。
_PAGE_REFS = {
    2019: {
        1: [1075, 1518],
        2: [1075, 1518],
    },
    2020: {
        2: [1032, 1525],
        5: [1020, 1522],
        6: [1029, 1526],
    },
    2021: {
        2: [1032, 1513],
        5: [1021, 1522],
        6: [1024, 1524],
        7: [1023, 1522],
    },
    2022: {
        1: [1028, 1529],
        2: [1029, 1525],
        5: [1028, 1523],
        6: [1027, 1527],
    },
    2023: {
        2: [1032, 1523],
        5: [1030, 1524],
        6: [1030, 1523],
    },
    2024: {
        2: [1036, 1523],
        3: [1037, 1526],
        6: [1035, 1523],
        7: [1034, 1525],
        8: [1034, 1522],
    },
}

_ANSWER_SCALES = {
    2019: (1.61, "原本指定の161%で配置（解答欄は実物大相当）"),
    2020: (1.61, "原本指定の161%で配置（解答欄は実物大相当）"),
    2021: (1.61, "原本指定の161%で配置（解答欄は実物大相当）"),
    2022: (1.58, "原本指定の158%で配置（解答欄は実物大相当）"),
    2023: (1.59, "原本指定の159%で配置（解答欄は実物大相当）"),
    2024: (1.56, "原本指定の156%で配置（解答欄は実物大相当）"),
}

# 大問単独の正解ではなく、その年度の数学全問の正解一覧を収録する。
_ALL_ANSWERS = {
    2019: [(1, [110, 365, 970, 735])],
    2020: [(5, [70, 360, 935, 745])],
    2021: [(5, [65, 365, 935, 775])],
    2022: [(5, [70, 365, 935, 725])],
    2023: [(5, [75, 365, 940, 750])],
    2024: [(6, [75, 370, 940, 750])],
}


def _piece(year: int, page: int, coords: list[int]) -> dict:
    return {"page": page, "box": coords, "ref_size": _PAGE_REFS[year][page]}


def _pieces(year: int, items: list[tuple[int, list[int]]]) -> list[dict]:
    return [_piece(year, page, coords) for page, coords in items]


def _config(
    *,
    year: int,
    question: int,
    grade: int,
    field: str,
    detail_unit: str,
    stamp: str,
    problem: list[tuple[int, list[int]]],
    answer_box: list[int],
    explanation: list[tuple[int, list[int]]],
    explanation_white_masks: list[list[list[float]]] | None = None,
    problem_page_groups: list[list[int]] | None = None,
) -> dict:
    answer_scale, answer_scale_label = _ANSWER_SCALES[year]
    filename = f"{year}年実施_静岡県_中{grade}数学_{detail_unit}.pdf"
    result = {
        "slug": f"shizuoka_q{question}_{year}",
        "repo": "local-source-shizuoka",
        "year": year,
        "session": "一般選抜",
        "prefecture": "静岡県",
        "question": question,
        "question_label": f"大問{question}",
        "grade": grade,
        "field": field,
        "detail_unit": detail_unit,
        "filename": filename,
        "stamp": stamp,
        "science_ref": _PAGE_REFS[year][problem[0][0]],
        **_SOURCES[year],
        "problem": _pieces(year, problem),
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
        "answers": _pieces(year, _ALL_ANSWERS[year]),
        "explanation": _pieces(year, explanation),
    }
    if explanation_white_masks is not None:
        if len(explanation_white_masks) != len(result["explanation"]):
            raise ValueError("explanation_white_masks must match explanation pieces")
        for item, masks in zip(result["explanation"], explanation_white_masks):
            item["white_masks"] = masks
    if problem_page_groups is not None:
        result["problem_page_groups"] = problem_page_groups
    return result


CONFIGS = [
    # 2019 ---------------------------------------------------------------
    _config(
        year=2019,
        question=3,
        grade=1,
        field="データの活用",
        detail_unit="資料の散らばりと代表値（相対度数・範囲・平均値・最頻値・中央値）",
        stamp="資料の散らばりと代表値 - 相対度数、範囲、平均値、最頻値、中央値",
        problem=[
            (1, [110, 1230, 970, 1500]),
            (2, [110, 130, 970, 465]),
        ],
        answer_box=[150, 775, 515, 827],
        explanation=[(2, [110, 350, 980, 680])],
        problem_page_groups=[[1, 2]],
    ),
    _config(
        year=2019,
        question=4,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（バスの道のり・速さ・休憩時間）",
        stamp="連立方程式の利用 - バスの道のり、速さ、休憩時間",
        problem=[(2, [110, 485, 970, 700])],
        answer_box=[120, 829, 515, 1380],
        explanation=[(2, [110, 700, 980, 1085])],
    ),

    # 2020 ---------------------------------------------------------------
    _config(
        year=2020,
        question=3,
        grade=1,
        field="データの活用",
        detail_unit="資料の散らばりと代表値（最頻値・範囲・中央値）",
        stamp="資料の散らばりと代表値 - 最頻値、範囲、中央値",
        problem=[(2, [90, 145, 955, 585])],
        answer_box=[150, 775, 515, 827],
        explanation=[(6, [95, 565, 975, 1015])],
    ),
    _config(
        year=2020,
        question=4,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（美術館の入館者数・割合・料金）",
        stamp="連立方程式の利用 - 美術館の入館者数、割合、料金",
        problem=[(2, [90, 595, 955, 875])],
        answer_box=[120, 825, 515, 1380],
        explanation=[(6, [95, 1035, 975, 1355])],
    ),

    # 2021 ---------------------------------------------------------------
    _config(
        year=2021,
        question=3,
        grade=1,
        field="データの活用",
        detail_unit="度数分布と代表値（ヒストグラム・最大値・中央値・平均値）",
        stamp="度数分布と代表値 - ヒストグラム、最大値、中央値、平均値",
        problem=[(2, [90, 135, 970, 640])],
        answer_box=[150, 735, 510, 842],
        explanation=[(6, [95, 655, 975, 1270])],
    ),
    _config(
        year=2021,
        question=4,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（可燃ごみとプラスチックごみ・割合）",
        stamp="連立方程式の利用 - 可燃ごみとプラスチックごみ、割合",
        problem=[(2, [90, 650, 970, 920])],
        answer_box=[150, 840, 510, 1390],
        explanation=[
            (6, [95, 1290, 975, 1425]),
            (7, [85, 160, 975, 305]),
        ],
    ),

    # 2022 ---------------------------------------------------------------
    _config(
        year=2022,
        question=3,
        grade=1,
        field="データの活用",
        detail_unit="資料の散らばりと代表値（範囲・平均値・中央値・資料の入れ替え）",
        stamp="資料の散らばりと代表値 - 範囲、平均値、中央値、資料の入れ替え",
        problem=[
            (1, [100, 1285, 975, 1510]),
            (2, [95, 140, 975, 695]),
        ],
        answer_box=[140, 740, 510, 845],
        explanation=[(6, [95, 570, 975, 1005])],
        problem_page_groups=[[1, 2]],
    ),
    _config(
        year=2022,
        question=4,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（メダカの移動・割合）",
        stamp="連立方程式の利用 - メダカの移動、割合",
        problem=[(2, [95, 705, 975, 900])],
        answer_box=[140, 845, 510, 1405],
        explanation=[(6, [95, 1025, 975, 1205])],
    ),

    # 2023 ---------------------------------------------------------------
    _config(
        year=2023,
        question=3,
        grade=2,
        field="データの活用",
        detail_unit="箱ひげ図と四分位数（中央値・四分位範囲・資料の追加）",
        stamp="箱ひげ図と四分位数 - 中央値、四分位範囲、資料の追加",
        problem=[(2, [90, 140, 975, 640])],
        answer_box=[160, 840, 530, 945],
        explanation=[(6, [90, 705, 975, 1210])],
    ),
    _config(
        year=2023,
        question=4,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（鉛筆とボールペン・割合）",
        stamp="連立方程式の利用 - 鉛筆とボールペン、割合",
        problem=[(2, [90, 650, 975, 925])],
        answer_box=[160, 945, 530, 1415],
        explanation=[(6, [90, 1225, 975, 1390])],
    ),

    # 2024 ---------------------------------------------------------------
    _config(
        year=2024,
        question=3,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（きゅうりとなす・袋詰め・割引）",
        stamp="連立方程式の利用 - きゅうりとなす、袋詰め、割引",
        problem=[(2, [100, 145, 980, 425])],
        answer_box=[140, 785, 515, 1299],
        explanation=[(7, [95, 805, 980, 1070])],
    ),
    _config(
        year=2024,
        question=5,
        grade=2,
        field="データの活用",
        detail_unit="相対度数分布表と箱ひげ図（累積相対度数・範囲・四分位数）",
        stamp="相対度数分布表と箱ひげ図 - 累積相対度数、範囲、四分位数",
        problem=[(3, [95, 140, 980, 1145])],
        answer_box=[590, 285, 960, 340],
        explanation=[(8, [75, 325, 980, 760])],
        # 前問（大問4）の図が原本上で右側へ回り込むため、その図だけを除去する。
        # 座標は上記crop内の正規化値で、左側の大問5本文には掛からない。
        explanation_white_masks=[[[0.69, 0.0, 1.0, 0.22]]],
    ),
]
