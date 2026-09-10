"""山形県・数学 採用2題の150dpi基準切り出し設定。

原本は ``D:\\Files\\(高校入試)山形県_2025`` に保存されている。
各年度の ``{year}_山形県_数学.pdf`` は問題と正解・解説を含み、
``{year}_山形県{year}解答用紙.pdf`` の1ページ目が数学の解答用紙である。

2020～2025年の数学問題・解説と解答用紙を全ページ目視確認し、問題文、
全設問、解説の途中式まで中学1・2年範囲で完結する2021年・2025年の
大問3だけを採用した。大問1・2は小問集合のため除外し、不採用年の
大問3と各年の大問4は、二次関数、三平方の定理、円、相似など
中学3年内容を含むため除外した。
座標はすべて原本を150dpiで描画して確認し、ページごとの画像寸法差を
各 ``ref_size`` に保持する。
"""

from __future__ import annotations

from pathlib import Path


SOURCE_ROOT = Path(r"D:\Files\(高校入試)山形県_2025")


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


def sources(year: int) -> dict:
    problem = (SOURCE_ROOT / f"{year}_山形県_数学.pdf").resolve()
    return {
        "problem_source_pdf": str(problem),
        "answer_source_pdf": str(
            (SOURCE_ROOT / f"{year}_山形県{year}解答用紙.pdf").resolve()
        ),
        "answers_source_pdf": str(problem),
        "explanation_source_pdf": str(problem),
    }


CONFIGS = [
    # 問題p3-4、正解p6、解説p8-9、解答用紙p1。
    {
        "slug": "yamagata_q3_2021_math",
        "year": 2021,
        "grade": 2,
        "prefecture": "山形県",
        "question": 3,
        "question_label": "大問3",
        "field": "関数",
        "detail_unit": "一次関数とグラフの利用（自動車・バス・移動距離）",
        "filename": (
            "2021年実施_山形県_中2数学_"
            "一次関数とグラフの利用（自動車・バス・移動距離）.pdf"
        ),
        "stamp": "一次関数とグラフの利用 - 自動車、バス、移動距離",
        "science_ref": [1031, 1521],
        **sources(2021),
        "problem": [
            fragment(3, (65, 1210, 965, 1420), (1031, 1521)),
            fragment(4, (75, 145, 965, 1385), (1029, 1518)),
        ],
        # 2断片は87%前後で同一A4面に収まる。自動分割でグラフを
        # 横切らないよう、原本2ページ分を1ページに固定する。
        "problem_page_groups": [[1, 2]],
        "answer_scale": 1.92,
        "answer_scale_label": (
            "原本指定の192%で配置（大問3の解答欄のみ）"
        ),
        "answer_sheet": [answer_fragment((185, 800, 520, 1215))],
        "answers": [
            fragment(6, (70, 360, 930, 955), (1033, 1520)),
        ],
        "explanation": [
            fragment(8, (65, 645, 970, 1510), (1033, 1520)),
            fragment(9, (65, 160, 975, 325), (1032, 1521)),
        ],
    },
    # 問題p3-5、正解p6、解説p8、解答用紙p1。
    {
        "slug": "yamagata_q3_2025_math",
        "year": 2025,
        "grade": 2,
        "prefecture": "山形県",
        "question": 3,
        "question_label": "大問3",
        "field": "関数",
        "detail_unit": "一次関数とグラフの利用（ロープウェイ・バス・標高）",
        "filename": (
            "2025年実施_山形県_中2数学_"
            "一次関数とグラフの利用（ロープウェイ・バス・標高）.pdf"
        ),
        "stamp": "一次関数とグラフの利用 - ロープウェイ、バス、標高",
        "science_ref": [1028, 1521],
        **sources(2025),
        "problem": [
            fragment(3, (70, 1175, 965, 1490), (1028, 1521)),
            # p4は図と問1の間の余白で分け、グラフを横切る自動分割を防ぐ。
            fragment(4, (70, 145, 965, 500), (1027, 1517)),
            fragment(4, (70, 500, 965, 1450), (1027, 1517)),
            fragment(5, (70, 145, 965, 250), (1028, 1520)),
        ],
        "problem_page_groups": [[1, 2], [3, 4]],
        "answer_scale": 1.89,
        "answer_scale_label": (
            "原本指定の189%で配置（大問3の解答欄のみ）"
        ),
        "answer_sheet": [answer_fragment((185, 795, 516, 1295))],
        "answers": [
            fragment(6, (68, 335, 922, 860), (1032, 1521)),
        ],
        "explanation": [
            fragment(8, (65, 535, 970, 1200), (1030, 1520)),
        ],
    },
]
