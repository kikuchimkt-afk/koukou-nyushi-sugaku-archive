"""沖縄県・数学 採用27題の150dpi基準切り出し設定。

問題・正解・解説は ``D:\\Files\\(高校入試)沖縄県`` のローカル原本を使う。
2019年だけ問題・正解・解説が合本 ``2019.pdf``、2020年以降は年度別の
``{year}_数学.pdf``。解答欄は各年度の ``Z47_{year}_解答用紙.pdf`` を使う。

座標はすべて原本を150dpiで描画して目視確認した値。ページごとの微妙な
画像サイズ差を吸収するため、問題・正解・解説の全断片に ``ref_size``、
解答欄の全断片に ``source_ref_size`` を明示している。
"""

from pathlib import Path


SOURCE_ROOT = Path(r"D:\Files\(高校入試)沖縄県")


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


def answer_fragment(
    bounds: tuple[int, int, int, int],
) -> dict:
    return {
        "page": 1,
        "box": box(*bounds),
        "source_ref_size": [1075, 1518],
        "rotation": 0,
    }


SCIENCE_REFS = {
    2019: [1075, 1518],
    2020: [1016, 1526],
    2021: [1019, 1526],
    2022: [1019, 1527],
    2023: [1022, 1523],
    2024: [1024, 1525],
}

ANSWER_SCALES = {
    2019: 1.64,
    2020: 1.67,
    2021: 1.64,
    2022: 1.56,
    2023: 1.56,
    2024: 1.59,
}

WHOLE_ANSWERS = {
    2019: [fragment(44, (110, 350, 965, 855), (1075, 1518))],
    2020: [fragment(9, (60, 350, 920, 900), (1019, 1523))],
    2021: [fragment(9, (60, 365, 920, 925), (1018, 1525))],
    2022: [fragment(8, (60, 355, 920, 865), (1019, 1523))],
    2023: [fragment(9, (60, 355, 920, 865), (1022, 1521))],
    2024: [fragment(9, (65, 355, 925, 900), (1023, 1520))],
}


def source_paths(year: int) -> dict[str, str]:
    problem_name = "2019.pdf" if year == 2019 else f"{year}_数学.pdf"
    return {
        "problem_source_pdf": str((SOURCE_ROOT / problem_name).resolve()),
        "answer_source_pdf": str(
            (SOURCE_ROOT / f"Z47_{year}_解答用紙.pdf").resolve()
        ),
    }


def config(
    *,
    year: int,
    question: int,
    grade: int,
    field: str,
    filename_unit: str,
    stamp: str,
    problem: list[dict],
    answer_sheet: list[dict],
    explanation: list[dict],
    science_dpi: int | None = None,
) -> dict:
    scale = ANSWER_SCALES[year]
    return {
        "slug": f"okinawa_q{question}_{year}_math",
        "year": year,
        "grade": grade,
        "prefecture": "沖縄県",
        "question": question,
        "question_label": f"大問{question}",
        "field": field,
        "filename": (
            f"{year}年実施_沖縄県_中{grade}数学_{filename_unit}.pdf"
        ),
        "stamp": stamp,
        "science_ref": SCIENCE_REFS[year],
        **({"science_dpi": science_dpi} if science_dpi is not None else {}),
        **source_paths(year),
        "problem": problem,
        "answer_scale": scale,
        "answer_scale_label": (
            f"原本指定の{round(scale * 100)}%で配置（該当大問の解答欄のみ）"
        ),
        "answer_sheet": answer_sheet,
        "answers": WHOLE_ANSWERS[year],
        "explanation": explanation,
    }


CONFIGS = [
    # 2019年（合本PDFの数学問題p1-6、数学正解p44、解説p45-47）
    config(
        year=2019,
        question=3,
        grade=1,
        field="データの活用",
        filename_unit="代表値とヒストグラム（平均値・中央値・最頻値）",
        stamp="代表値とヒストグラム - 平均値、中央値、最頻値",
        problem=[fragment(2, (125, 295, 970, 1140), (1075, 1518))],
        answer_sheet=[answer_fragment((112, 870, 395, 981))],
        explanation=[fragment(45, (105, 390, 970, 630), (1075, 1518))],
    ),
    config(
        year=2019,
        question=4,
        grade=1,
        field="図形",
        filename_unit="垂直二等分線の作図（2点から等距離の点）",
        stamp="垂直二等分線の作図 - 2点から等距離の点",
        problem=[fragment(2, (125, 1150, 970, 1450), (1075, 1518))],
        answer_sheet=[answer_fragment((112, 978, 461, 1341))],
        explanation=[fragment(45, (105, 630, 970, 770), (1075, 1518))],
    ),
    config(
        year=2019,
        question=5,
        grade=2,
        field="データの活用",
        filename_unit="確率と相対度数（カードの復元抽出・積の余り）",
        stamp="確率と相対度数 - カードの復元抽出、積の余り",
        problem=[fragment(3, (125, 130, 970, 880), (1075, 1518))],
        answer_sheet=[answer_fragment((489, 292, 774, 475))],
        explanation=[fragment(45, (105, 775, 970, 1190), (1075, 1518))],
    ),
    config(
        year=2019,
        question=6,
        grade=2,
        field="関数",
        filename_unit="一次関数の利用（電気料金プランの比較）",
        stamp="一次関数の利用 - 電気料金プランの比較",
        problem=[
            fragment(3, (125, 895, 970, 1450), (1075, 1518)),
            fragment(4, (125, 140, 970, 220), (1075, 1518)),
        ],
        answer_sheet=[answer_fragment((489, 472, 774, 583))],
        explanation=[
            fragment(45, (105, 1190, 970, 1450), (1075, 1518)),
            fragment(46, (105, 145, 970, 510), (1075, 1518)),
        ],
    ),
    config(
        year=2019,
        question=10,
        grade=2,
        field="規則性",
        filename_unit="規則性（円形に並べた駒の裏返し）",
        stamp="規則性 - 円形に並べた駒の裏返し",
        problem=[
            fragment(5, (120, 1080, 970, 1450), (1075, 1518)),
            fragment(6, (120, 140, 970, 1245), (1075, 1518)),
        ],
        answer_sheet=[answer_fragment((489, 1194, 775, 1341))],
        explanation=[fragment(47, (105, 490, 970, 820), (1075, 1518))],
    ),

    # 2020年
    config(
        year=2020,
        question=3,
        grade=2,
        field="データの活用",
        filename_unit="場合の数と確率（カード2枚でつくる整数）",
        stamp="場合の数と確率 - カード2枚でつくる整数",
        problem=[fragment(2, (70, 590, 910, 1090), (1018, 1525))],
        answer_sheet=[answer_fragment((117, 928, 396, 1037))],
        explanation=[fragment(10, (105, 1090, 960, 1375), (1018, 1524))],
    ),
    config(
        year=2020,
        question=4,
        grade=1,
        field="図形",
        filename_unit="作図と対称移動（線分の長さの和）",
        stamp="作図と対称移動 - 線分の長さの和",
        problem=[
            fragment(2, (70, 1100, 950, 1450), (1018, 1525)),
            fragment(3, (115, 145, 950, 440), (1020, 1526)),
        ],
        answer_sheet=[answer_fragment((117, 1034, 461, 1375))],
        explanation=[
            fragment(10, (65, 1370, 960, 1450), (1018, 1524)),
            fragment(11, (80, 160, 920, 960), (1018, 1522)),
        ],
    ),
    config(
        year=2020,
        question=5,
        grade=2,
        field="規則性",
        filename_unit="文字式による説明（カレンダーの5数の和）",
        stamp="文字式による説明 - カレンダーの5数の和",
        problem=[
            fragment(3, (115, 465, 950, 1410), (1020, 1526)),
            fragment(4, (90, 145, 910, 545), (1018, 1523)),
        ],
        answer_sheet=[answer_fragment((490, 289, 769, 504))],
        explanation=[
            fragment(11, (65, 970, 600, 1015), (1018, 1522)),
            fragment(11, (65, 1015, 920, 1405), (1018, 1522)),
        ],
        science_dpi=1300,
    ),
    config(
        year=2020,
        question=6,
        grade=2,
        field="関数",
        filename_unit="一次関数と動点（直角三角形の面積）",
        stamp="一次関数と動点 - 直角三角形の面積",
        problem=[
            fragment(4, (75, 555, 920, 1410), (1018, 1523)),
            fragment(5, (115, 145, 950, 220), (1020, 1526)),
        ],
        answer_sheet=[answer_fragment((490, 502, 769, 646))],
        explanation=[fragment(12, (105, 165, 960, 655), (1018, 1524))],
    ),
    config(
        year=2020,
        question=8,
        grade=2,
        field="図形の証明",
        filename_unit="平行四辺形と合同の証明（面積比）",
        stamp="平行四辺形と合同の証明 - 面積比",
        problem=[
            fragment(5, (110, 1035, 950, 1450), (1020, 1526)),
            fragment(6, (70, 155, 920, 825), (1014, 1522)),
        ],
        answer_sheet=[answer_fragment((490, 785, 894, 1107))],
        explanation=[
            fragment(12, (105, 1115, 960, 1450), (1018, 1524)),
            fragment(13, (105, 160, 920, 245), (1019, 1522)),
        ],
    ),
    config(
        year=2020,
        question=10,
        grade=2,
        field="規則性",
        filename_unit="操作の規則性（命令・余り・周期）",
        stamp="操作の規則性 - 命令、余り、周期",
        problem=[
            fragment(7, (110, 520, 950, 1405), (1019, 1525)),
            fragment(8, (90, 160, 920, 990), (1018, 1524)),
        ],
        answer_sheet=[answer_fragment((490, 1212, 771, 1375))],
        explanation=[
            fragment(13, (65, 1050, 920, 1450), (1019, 1522)),
            fragment(14, (105, 160, 960, 875), (1018, 1523)),
        ],
    ),

    # 2021年
    config(
        year=2021,
        question=3,
        grade=2,
        field="データの活用",
        filename_unit="場合の数と確率（2個のさいころ・座標）",
        stamp="場合の数と確率 - 2個のさいころ、座標",
        problem=[fragment(2, (115, 715, 950, 1420), (1020, 1527))],
        answer_sheet=[answer_fragment((114, 876, 397, 986))],
        explanation=[fragment(10, (105, 495, 960, 745), (1018, 1526))],
    ),
    config(
        year=2021,
        question=4,
        grade=2,
        field="図形",
        filename_unit="角の二等分線の作図（平行線・二等辺三角形）",
        stamp="角の二等分線の作図 - 平行線、二等辺三角形",
        problem=[fragment(3, (75, 135, 950, 725), (1019, 1525))],
        answer_sheet=[answer_fragment((114, 984, 464, 1381))],
        explanation=[fragment(10, (105, 750, 960, 980), (1018, 1526))],
    ),
    config(
        year=2021,
        question=5,
        grade=2,
        field="規則性",
        filename_unit="文字式による説明（2けたの数・11の倍数）",
        stamp="文字式による説明 - 2けたの数、11の倍数",
        problem=[
            fragment(3, (75, 745, 950, 1410), (1019, 1525)),
            fragment(4, (110, 155, 950, 575), (1021, 1527)),
        ],
        answer_sheet=[answer_fragment((492, 299, 775, 482))],
        explanation=[fragment(10, (105, 995, 960, 1290), (1018, 1526))],
    ),
    config(
        year=2021,
        question=10,
        grade=1,
        field="数と式",
        filename_unit="最大公約数（長方形の正方形分割）",
        stamp="最大公約数 - 長方形の正方形分割",
        problem=[
            fragment(7, (80, 490, 920, 1410), (1019, 1525)),
            fragment(8, (100, 150, 950, 800), (1020, 1527)),
        ],
        answer_sheet=[answer_fragment((492, 1271, 778, 1381))],
        explanation=[fragment(12, (105, 400, 960, 860), (1019, 1526))],
    ),

    # 2022年
    config(
        year=2022,
        question=3,
        grade=2,
        field="データの活用",
        filename_unit="場合の数と確率（2回の玉の取り出し・数直線）",
        stamp="場合の数と確率 - 2回の玉の取り出し、数直線",
        problem=[
            fragment(2, (75, 645, 910, 1405), (1020, 1524)),
            fragment(3, (120, 140, 940, 250), (1019, 1525)),
        ],
        answer_sheet=[answer_fragment((98, 915, 394, 1031))],
        explanation=[fragment(9, (105, 325, 960, 570), (1017, 1525))],
    ),
    config(
        year=2022,
        question=4,
        grade=2,
        field="図形",
        filename_unit="作図（平行四辺形・垂直二等分線）",
        stamp="作図 - 平行四辺形、垂直二等分線",
        problem=[fragment(3, (115, 265, 950, 1165), (1019, 1525))],
        answer_sheet=[answer_fragment((98, 1028, 462, 1370))],
        explanation=[fragment(9, (105, 580, 960, 720), (1017, 1525))],
    ),
    config(
        year=2022,
        question=6,
        grade=2,
        field="関数",
        filename_unit="一次関数の利用（マスク注文料金の比較）",
        stamp="一次関数の利用 - マスク注文料金の比較",
        problem=[
            fragment(4, (70, 905, 920, 1410), (1021, 1524)),
            fragment(5, (120, 145, 950, 750), (1019, 1525)),
        ],
        answer_sheet=[answer_fragment((493, 499, 790, 615))],
        explanation=[fragment(9, (105, 970, 960, 1300), (1017, 1525))],
    ),
    config(
        year=2022,
        question=9,
        grade=1,
        field="図形",
        filename_unit="球・円柱・円すい（表面積と体積）",
        stamp="球、円柱、円すい - 表面積と体積",
        problem=[fragment(6, (70, 620, 920, 1150), (1019, 1525))],
        answer_sheet=[answer_fragment((493, 1086, 790, 1238))],
        explanation=[fragment(10, (65, 845, 920, 1090), (1022, 1523))],
    ),

    # 2023年
    config(
        year=2023,
        question=3,
        grade=2,
        field="データの活用",
        filename_unit="箱ひげ図と四分位範囲（気温データ）",
        stamp="箱ひげ図と四分位範囲 - 気温データ",
        problem=[
            fragment(2, (75, 620, 910, 1410), (1022, 1522)),
            fragment(3, (120, 145, 960, 410), (1021, 1523)),
        ],
        answer_sheet=[answer_fragment((93, 778, 428, 894))],
        explanation=[fragment(10, (105, 440, 960, 700), (1020, 1523))],
    ),
    config(
        year=2023,
        question=4,
        grade=2,
        field="データの活用",
        filename_unit="場合の数と確率（2個のさいころ・2けたの整数）",
        stamp="場合の数と確率 - 2個のさいころ、2けたの整数",
        problem=[fragment(3, (120, 425, 960, 740), (1021, 1523))],
        answer_sheet=[answer_fragment((93, 892, 428, 1008))],
        explanation=[fragment(10, (105, 710, 960, 930), (1020, 1523))],
    ),
    config(
        year=2023,
        question=5,
        grade=2,
        field="関数",
        filename_unit="一次関数の利用（電話料金プランの比較）",
        stamp="一次関数の利用 - 電話料金プランの比較",
        problem=[
            fragment(3, (120, 745, 960, 1410), (1021, 1523)),
            fragment(4, (90, 145, 920, 570), (1023, 1521)),
        ],
        answer_sheet=[answer_fragment((93, 1006, 428, 1121))],
        explanation=[fragment(10, (105, 935, 960, 1210), (1020, 1523))],
    ),
    config(
        year=2023,
        question=7,
        grade=1,
        field="図形",
        filename_unit="角の二等分線の作図（三角形）",
        stamp="角の二等分線の作図 - 三角形",
        problem=[fragment(5, (115, 390, 950, 690), (1022, 1523))],
        answer_sheet=[answer_fragment((93, 1157, 427, 1422))],
        explanation=[fragment(11, (65, 165, 920, 305), (1020, 1521))],
    ),

    # 2024年
    config(
        year=2024,
        question=3,
        grade=2,
        field="データの活用",
        filename_unit="箱ひげ図と四分位範囲（降水日数の比較）",
        stamp="箱ひげ図と四分位範囲 - 降水日数の比較",
        problem=[
            fragment(2, (80, 525, 920, 1410), (1025, 1523)),
            fragment(3, (115, 145, 920, 595), (1024, 1524)),
        ],
        answer_sheet=[answer_fragment((102, 771, 431, 886))],
        explanation=[fragment(10, (105, 455, 960, 845), (1022, 1522))],
    ),
    config(
        year=2024,
        question=4,
        grade=2,
        field="データの活用",
        filename_unit="場合の数と確率（プレゼント交換の順列）",
        stamp="場合の数と確率 - プレゼント交換の順列",
        problem=[fragment(3, (115, 615, 950, 1045), (1024, 1524))],
        answer_sheet=[answer_fragment((102, 884, 431, 996))],
        explanation=[fragment(10, (105, 850, 960, 1165), (1022, 1522))],
    ),
    config(
        year=2024,
        question=5,
        grade=2,
        field="関数",
        filename_unit="一次関数の利用（卒業文集の料金比較）",
        stamp="一次関数の利用 - 卒業文集の料金比較",
        problem=[
            fragment(3, (115, 1060, 950, 1410), (1024, 1524)),
            fragment(4, (90, 145, 920, 915), (1025, 1524)),
        ],
        answer_sheet=[answer_fragment((102, 993, 431, 1107))],
        explanation=[fragment(10, (105, 1170, 960, 1410), (1022, 1522))],
    ),
    config(
        year=2024,
        question=7,
        grade=1,
        field="図形",
        filename_unit="垂線の作図（三角形の高さ）",
        stamp="垂線の作図 - 三角形の高さ",
        problem=[fragment(5, (115, 1035, 950, 1410), (1024, 1525))],
        answer_sheet=[answer_fragment((102, 1141, 431, 1410))],
        explanation=[
            fragment(11, (65, 405, 615, 610), (1023, 1521)),
            fragment(11, (620, 360, 920, 625), (1023, 1521)),
        ],
        science_dpi=2300,
    ),
]
