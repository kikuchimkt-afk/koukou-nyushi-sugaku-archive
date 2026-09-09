"""岐阜県 2018〜2023年・採用14題の150dpi基準切り出し設定。

原本は ``D:\\Files\\(高校入試)_岐阜県`` に保存された通常の本検査。
問題文・全設問・解説途中式のどこにも中3内容を含まない独立大問だけを
採用し、小問集合は除外した。採用設定は ``configs.py`` から読み込む。

2018年だけ問題・解答用紙・解説が別PDFで、2019年以降は数学PDFの中に
問題、全問の正解一覧、解説が収録されている。ページごとの画像寸法差を
吸収するため、全断片に150dpiで実測した ``ref_size`` を付ける。
"""

from __future__ import annotations


_ROOT = r"D:\Files\(高校入試)_岐阜県"

_SOURCES = {
    2018: {
        "problem_source_pdf": _ROOT + r"\2018(H30)_問題.pdf",
        "answer_source_pdf": _ROOT + r"\2018(H30)_解答用紙].pdf",
        "answers_source_pdf": _ROOT + r"\2018(H30)_解説.pdf",
        "explanation_source_pdf": _ROOT + r"\2018(H30)_解説.pdf",
    },
    2019: {
        "problem_source_pdf": _ROOT + r"\2019_数学.pdf",
        "answer_source_pdf": _ROOT + r"\2019_解答用紙.pdf",
        "answers_source_pdf": _ROOT + r"\2019_数学.pdf",
        "explanation_source_pdf": _ROOT + r"\2019_数学.pdf",
    },
    2020: {
        "problem_source_pdf": _ROOT + r"\2020_数学.pdf",
        "answer_source_pdf": _ROOT + r"\2020_解答用紙.pdf",
        "answers_source_pdf": _ROOT + r"\2020_数学.pdf",
        "explanation_source_pdf": _ROOT + r"\2020_数学.pdf",
    },
    2021: {
        "problem_source_pdf": _ROOT + r"\2021_数学.pdf",
        "answer_source_pdf": _ROOT + r"\2021_解答用紙.pdf",
        "answers_source_pdf": _ROOT + r"\2021_数学.pdf",
        "explanation_source_pdf": _ROOT + r"\2021_数学.pdf",
    },
    2022: {
        "problem_source_pdf": _ROOT + r"\2022_数学.pdf",
        "answer_source_pdf": _ROOT + r"\2022_解答用紙.pdf",
        "answers_source_pdf": _ROOT + r"\2022_数学.pdf",
        "explanation_source_pdf": _ROOT + r"\2022_数学.pdf",
    },
    2023: {
        "problem_source_pdf": _ROOT + r"\2023_数学.pdf",
        "answer_source_pdf": _ROOT + r"\2023_解答用紙.pdf",
        "answers_source_pdf": _ROOT + r"\2023_数学.pdf",
        "explanation_source_pdf": _ROOT + r"\2023_数学.pdf",
    },
}

# pdftoppm -r 150 でレンダリングした各数学・解説ページの実寸。
_PAGE_REFS = {
    2018: {
        1: [1075, 1518],
        2: [1075, 1518],
        3: [1075, 1518],
        4: [1075, 1518],
    },
    2019: {
        1: [1003, 1528],
        2: [1003, 1528],
        3: [1003, 1529],
        4: [1002, 1527],
        5: [1005, 1526],
        6: [1005, 1528],
        7: [1006, 1526],
    },
    2020: {
        1: [999, 1529],
        2: [999, 1528],
        3: [998, 1529],
        4: [999, 1528],
        5: [999, 1525],
        6: [1001, 1526],
        7: [999, 1527],
    },
    2021: {
        1: [996, 1527],
        2: [994, 1528],
        3: [1013, 1528],
        4: [994, 1529],
        5: [1014, 1527],
        6: [997, 1527],
        7: [1014, 1527],
    },
    2022: {
        1: [994, 1525],
        2: [996, 1523],
        3: [994, 1524],
        4: [995, 1525],
        5: [996, 1525],
        6: [996, 1525],
        7: [1013, 1525],
    },
    2023: {
        1: [992, 1527],
        2: [993, 1525],
        3: [994, 1525],
        4: [994, 1525],
        5: [994, 1525],
        6: [993, 1526],
        7: [1014, 1524],
        8: [994, 1526],
    },
}

_ANSWER_SCALES = {
    2018: (1.00, "原本に拡大率指定なし（100%で配置）"),
    2019: (1.00, "原本に拡大率指定なし（100%で配置）"),
    2020: (1.27, "原本指定の127%で配置（解答欄は実物大相当）"),
    2021: (1.32, "原本指定の132%で配置（解答欄は実物大相当）"),
    2022: (1.32, "原本指定の132%で配置（解答欄は実物大相当）"),
    2023: (1.32, "原本指定の132%で配置（解答欄は実物大相当）"),
}

_ALL_ANSWERS = {
    2018: [(1, [95, 340, 990, 710])],
    2019: [(5, [35, 340, 970, 725])],
    2020: [(5, [35, 350, 965, 740])],
    2021: [(5, [50, 360, 930, 725])],
    2022: [(5, [35, 355, 920, 760])],
    2023: [(5, [35, 350, 920, 700])],
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
    filename: str,
    stamp: str,
    problem: list[tuple[int, list[int]]],
    answer_box: list[int],
    explanation: list[tuple[int, list[int]]],
) -> dict:
    answer_scale, answer_scale_label = _ANSWER_SCALES[year]
    return {
        "slug": f"gifu_q{question}_{year}",
        "repo": "local-source-gifu",
        "year": year,
        "session": "本検査",
        "prefecture": "岐阜県",
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
        # 大問ごとの正解だけでなく、その年度の数学全問の正解一覧を収録する。
        "answers": _pieces(year, _ALL_ANSWERS[year]),
        "explanation": _pieces(year, explanation),
    }


CONFIGS = [
    # 2018 ---------------------------------------------------------------
    _config(
        year=2018,
        question=2,
        grade=1,
        field="データの活用",
        detail_unit="度数分布と代表値（ヒストグラム・中央値・相対度数）",
        filename="2018年実施_岐阜県_中1数学_度数分布と代表値（ヒストグラム・中央値・相対度数）.pdf",
        stamp="度数分布と代表値 - ヒストグラム、中央値、相対度数",
        problem=[(2, [105, 975, 970, 1395])],
        answer_box=[135, 325, 790, 405],
        explanation=[
            (1, [100, 1195, 985, 1432]),
            (2, [100, 164, 985, 195]),
        ],
    ),
    _config(
        year=2018,
        question=4,
        grade=2,
        field="関数",
        detail_unit="一次関数のグラフの利用（往復の道のりと追いつき）",
        filename="2018年実施_岐阜県_中2数学_一次関数の利用（往復の道のりと追いつき）.pdf",
        stamp="一次関数の利用 - 往復の道のり、すれ違い、追いつき",
        problem=[(3, [110, 370, 970, 995])],
        answer_box=[135, 480, 945, 790],
        explanation=[(2, [100, 450, 985, 970])],
    ),

    # 2019 ---------------------------------------------------------------
    _config(
        year=2019,
        question=3,
        grade=2,
        field="データの活用",
        detail_unit="場合の数と確率（玉の復元抽出・色と数字）",
        filename="2019年実施_岐阜県_中2数学_場合の数と確率（玉の復元抽出・色と数字）.pdf",
        stamp="場合の数と確率 - 玉の復元抽出、色と数字",
        problem=[(2, [55, 555, 950, 875])],
        answer_box=[145, 575, 760, 655],
        explanation=[(6, [45, 160, 970, 490])],
    ),
    _config(
        year=2019,
        question=4,
        grade=2,
        field="方程式の利用",
        detail_unit="連立方程式の利用（機械の生産量と割合）",
        filename="2019年実施_岐阜県_中2数学_連立方程式の利用（機械の生産量と割合）.pdf",
        stamp="連立方程式の利用 - 機械の生産量と割合",
        problem=[
            (2, [55, 875, 950, 1397]),
            (3, [115, 152, 950, 640]),
        ],
        answer_box=[145, 665, 825, 840],
        explanation=[(6, [45, 490, 970, 850])],
    ),
    _config(
        year=2019,
        question=6,
        grade=2,
        field="規則性",
        detail_unit="規則性と文字式（正方形カード・周の長さ・総数）",
        filename="2019年実施_岐阜県_中2数学_規則性と文字式（正方形カード・周の長さ・総数）.pdf",
        stamp="規則性と文字式 - 正方形カード、周の長さ、総数",
        problem=[(4, [50, 270, 950, 1410])],
        answer_box=[145, 1260, 950, 1395],
        explanation=[(7, [45, 160, 970, 590])],
    ),

    # 2020 ---------------------------------------------------------------
    _config(
        year=2020,
        question=2,
        grade=1,
        field="データの活用",
        detail_unit="度数分布表と代表値（最頻値・中央値・相対度数・範囲）",
        filename="2020年実施_岐阜県_中1数学_度数分布表と代表値（最頻値・中央値・相対度数・範囲）.pdf",
        stamp="度数分布表と代表値 - 最頻値、中央値、相対度数、範囲",
        problem=[
            (1, [105, 1035, 960, 1462]),
            (2, [75, 156, 900, 295]),
        ],
        answer_box=[140, 318, 750, 390],
        explanation=[
            (5, [40, 1200, 970, 1443]),
            (6, [40, 178, 970, 290]),
        ],
    ),
    _config(
        year=2020,
        question=4,
        grade=2,
        field="関数",
        detail_unit="一次関数のグラフの利用（給水と水面の高さ）",
        filename="2020年実施_岐阜県_中2数学_一次関数の利用（給水と水面の高さ）.pdf",
        stamp="一次関数の利用 - 給水、水面の高さ、グラフ",
        problem=[
            (2, [55, 910, 950, 1495]),
            (3, [105, 145, 960, 580]),
        ],
        answer_box=[140, 510, 940, 835],
        explanation=[(6, [95, 510, 970, 1180])],
    ),

    # 2021 ---------------------------------------------------------------
    _config(
        year=2021,
        question=2,
        grade=1,
        field="関数",
        detail_unit="反比例の利用（電子レンジの出力と調理時間）",
        filename="2021年実施_岐阜県_中1数学_反比例の利用（電子レンジの出力と調理時間）.pdf",
        stamp="反比例の利用 - 電子レンジの出力と調理時間",
        problem=[(2, [100, 590, 960, 870])],
        answer_box=[125, 470, 465, 575],
        # 原本見出しは「比例関数」だが、本文・式・途中式は一貫して反比例。
        explanation=[
            (5, [50, 1295, 960, 1444]),
            (6, [90, 176, 970, 235]),
        ],
    ),
    _config(
        year=2021,
        question=3,
        grade=2,
        field="データの活用",
        detail_unit="場合の数と確率（2個のさいころ・直線）",
        filename="2021年実施_岐阜県_中2数学_場合の数と確率（2個のさいころ・直線）.pdf",
        stamp="場合の数と確率 - 2個のさいころと直線",
        problem=[(2, [100, 875, 960, 1180])],
        answer_box=[125, 575, 465, 730],
        explanation=[(6, [90, 235, 970, 610])],
    ),
    _config(
        year=2021,
        question=4,
        grade=2,
        field="関数",
        detail_unit="一次関数のグラフの利用（セロハンの折り返しと面積）",
        filename="2021年実施_岐阜県_中2数学_一次関数の利用（セロハンの折り返しと面積）.pdf",
        stamp="一次関数の利用 - セロハンの折り返し、面積、グラフ",
        problem=[
            (2, [100, 1195, 960, 1495]),
            (3, [80, 140, 930, 770]),
        ],
        answer_box=[515, 205, 965, 730],
        explanation=[(6, [90, 610, 970, 1085])],
    ),

    # 2022 ---------------------------------------------------------------
    _config(
        year=2022,
        question=3,
        grade=1,
        field="データの活用",
        detail_unit="度数分布と代表値（平均値・中央値・資料の追加）",
        filename="2022年実施_岐阜県_中1数学_度数分布と代表値（平均値・中央値・資料の追加）.pdf",
        stamp="度数分布と代表値 - 平均値、中央値、資料の追加",
        problem=[
            (1, [105, 1285, 965, 1398]),
            (2, [55, 153, 900, 550]),
        ],
        answer_box=[105, 595, 455, 735],
        explanation=[(6, [90, 420, 970, 695])],
    ),

    # 2023 ---------------------------------------------------------------
    _config(
        year=2023,
        question=3,
        grade=2,
        field="データの活用",
        detail_unit="箱ひげ図と四分位数（四分位範囲・2群の比較）",
        filename="2023年実施_岐阜県_中2数学_箱ひげ図と四分位数（四分位範囲・2群の比較）.pdf",
        stamp="箱ひげ図と四分位数 - 四分位範囲、2群の比較",
        problem=[(2, [40, 140, 930, 790])],
        answer_box=[525, 355, 875, 490],
        explanation=[(6, [80, 610, 960, 1300])],
    ),
    _config(
        year=2023,
        question=4,
        grade=2,
        field="関数",
        detail_unit="一次関数のグラフの利用（モノレール・すれ違い・追い越し）",
        filename="2023年実施_岐阜県_中2数学_一次関数の利用（モノレール・すれ違い・追い越し）.pdf",
        stamp="一次関数の利用 - モノレール、すれ違い、追い越し",
        problem=[
            (2, [40, 810, 930, 1447]),
            (3, [105, 149, 960, 405]),
        ],
        answer_box=[525, 500, 875, 710],
        explanation=[
            (6, [80, 1300, 960, 1438]),
            (7, [70, 171, 930, 895]),
        ],
    ),
    _config(
        year=2023,
        question=6,
        grade=2,
        field="規則性",
        detail_unit="数の性質と文字式（各位の数の和・3けたの自然数）",
        filename="2023年実施_岐阜県_中2数学_数の性質と文字式（各位の数の和・3けたの自然数）.pdf",
        stamp="数の性質と文字式 - 各位の数の和、3けたの自然数",
        problem=[
            (3, [105, 1150, 960, 1378]),
            (4, [55, 152, 900, 890]),
        ],
        answer_box=[610, 810, 960, 1110],
        explanation=[
            (7, [40, 1350, 930, 1426]),
            (8, [90, 174, 970, 770]),
        ],
    ),
]
