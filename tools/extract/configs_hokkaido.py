"""北海道・数学 採用8題の150dpi基準切り出し設定。

元PDFはすべて koukou-nyushi-hokkaido/public/files/{year}/ 配下。
このファイルは測定結果の引き渡し用で、数学アプリ本体には未適用。
"""


def box(x1: int, y1: int, x2: int, y2: int) -> list[int]:
    return [x1, y1, x2, y2]


CONFIGS = [
    {
        "slug": "hokkaido_q3_2018_math",
        "year": 2018,
        "grade": 1,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "データの活用",
        "filename": "2018年実施_北海道_中1数学_度数分布表と代表値（相対度数・平均値・中央値・階級）.pdf",
        "stamp": "度数分布表と代表値 - 相対度数、平均値、中央値、階級",
        "science_ref": [1075, 1518],
        "problem": [
            {"page": 3, "box": box(105, 115, 970, 1210)},
        ],
        "answer_scale": 1.68,
        "answer_scale_label": "原本指定の168%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(535, 180, 890, 360),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        # 2018原本には2019年以降のような独立した「数学解答」一覧がない。
        # 全問の正解を欠かさない代替として、数学の解答・解説全体を収録する。
        "answers": [
            {"page": 6, "box": box(105, 150, 970, 1505)},
            {"page": 7, "box": box(105, 150, 970, 1420)},
        ],
        "explanation": [
            {"page": 6, "box": box(105, 815, 970, 1008)},
        ],
    },
    {
        "slug": "hokkaido_q3_2019_math",
        "year": 2019,
        "grade": 2,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "規則性",
        "filename": "2019年実施_北海道_中2数学_文字式による説明（ます目の和・単項式・方程式の応用）.pdf",
        "stamp": "文字式による説明 - ます目の和、単項式、方程式の応用",
        "science_ref": [1023, 1518],
        "problem": [
            {"page": 2, "box": box(75, 965, 940, 1395)},
            {"page": 3, "box": box(115, 145, 950, 595), "ref_size": [1024, 1520]},
        ],
        "answer_scale": 1.67,
        "answer_scale_label": "原本指定の167%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(150, 890, 510, 985),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.0, 0.25, 0.09, 1.0]],
            },
            {
                "page": 1,
                "box": box(535, 210, 890, 435),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(65, 365, 925, 835), "ref_size": [1025, 1518]},
        ],
        "explanation": [
            {"page": 7, "box": box(105, 750, 965, 1215), "ref_size": [1025, 1520]},
        ],
    },
    {
        "slug": "hokkaido_q5_2019_math",
        "year": 2019,
        "grade": 2,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 5,
        "field": "図形の証明",
        "filename": "2019年実施_北海道_中2数学_台形と合同の証明（角度・垂線・三角形の合同）.pdf",
        "stamp": "台形と合同の証明 - 角度、垂線、三角形の合同",
        "science_ref": [1023, 1519],
        # p4上部の通常問題Q5だけ。直後の黒帯「学校裁量問題」は含めない。
        "problem": [
            {"page": 4, "box": box(75, 140, 930, 480)},
        ],
        "answer_scale": 1.67,
        "answer_scale_label": "原本指定の167%で配置（通常問題Q5の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(535, 755, 890, 1138),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(65, 365, 925, 835), "ref_size": [1025, 1518]},
        ],
        "explanation": [
            {"page": 8, "box": box(65, 350, 950, 590), "ref_size": [1024, 1518]},
        ],
    },
    {
        "slug": "hokkaido_q3_2020_math",
        "year": 2020,
        "grade": 2,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "規則性",
        "filename": "2020年実施_北海道_中2数学_整数の性質と文字式（倍数・カレンダー・うるう年の周期）.pdf",
        "stamp": "整数の性質と文字式 - 倍数、カレンダー、うるう年の周期",
        "science_ref": [1019, 1523],
        "problem": [
            {"page": 3, "box": box(120, 300, 950, 1140)},
            {"page": 4, "box": box(120, 155, 950, 695), "ref_size": [1018, 1521]},
        ],
        "answer_scale": 1.67,
        "answer_scale_label": "原本指定の167%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(530, 210, 890, 345),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": box(60, 360, 915, 985), "ref_size": [1020, 1521]},
        ],
        "explanation": [
            {"page": 8, "box": box(110, 1085, 965, 1505), "ref_size": [1021, 1522]},
            {"page": 9, "box": box(105, 155, 965, 305), "ref_size": [1021, 1520]},
        ],
    },
    {
        "slug": "hokkaido_q3_2021_math",
        "year": 2021,
        "grade": 2,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "規則性",
        "filename": "2021年実施_北海道_中2数学_規則性と文字式（ストロー・五角形・正六角形・説明）.pdf",
        "stamp": "規則性と文字式 - ストロー、五角形、正六角形、説明",
        "science_ref": [1021, 1519],
        "problem": [
            {"page": 3, "box": box(75, 140, 930, 1335)},
            {"page": 4, "box": box(115, 145, 930, 600), "ref_size": [1018, 1521]},
        ],
        "answer_scale": 1.59,
        "answer_scale_label": "原本指定の159%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(140, 1065, 510, 1170),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.0, 0.25, 0.09, 1.0]],
            },
            {
                "page": 1,
                "box": box(540, 240, 905, 485),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(60, 355, 915, 950), "ref_size": [1021, 1517]},
        ],
        "explanation": [
            {"page": 9, "box": box(105, 1340, 960, 1505), "ref_size": [1019, 1519]},
            {"page": 10, "box": box(105, 150, 955, 700), "ref_size": [1021, 1517]},
        ],
    },
    {
        "slug": "hokkaido_q5_2021_math",
        "year": 2021,
        "grade": 2,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 5,
        "field": "図形の証明",
        "filename": "2021年実施_北海道_中2数学_台形と合同の証明（対角線・平行線と角・線分の相等）.pdf",
        "stamp": "台形と合同の証明 - 対角線、平行線と角、線分の相等",
        "science_ref": [1021, 1519],
        # p5上部の通常問題Q5だけ。直後の黒帯「学校裁量問題」は含めない。
        "problem": [
            {"page": 5, "box": box(75, 140, 915, 640)},
        ],
        "answer_scale": 1.59,
        "answer_scale_label": "原本指定の159%で配置（通常問題Q5の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(535, 880, 910, 1260),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(60, 355, 915, 950), "ref_size": [1021, 1517]},
        ],
        "explanation": [
            {"page": 10, "box": box(65, 1295, 960, 1505), "ref_size": [1021, 1517]},
            {"page": 11, "box": box(135, 165, 955, 265), "ref_size": [1018, 1519]},
        ],
    },
    {
        "slug": "hokkaido_q2_2022_math",
        "year": 2022,
        "grade": 2,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 2,
        "field": "データの活用",
        "filename": "2022年実施_北海道_中2数学_箱ひげ図と四分位数（第3四分位数・範囲・中央値・分布）.pdf",
        "stamp": "箱ひげ図と四分位数 - 第3四分位数、範囲、中央値、分布",
        "science_ref": [1021, 1518],
        "problem": [
            {"page": 2, "box": box(75, 140, 930, 1505)},
            {"page": 3, "box": box(135, 145, 950, 485), "ref_size": [1020, 1520]},
        ],
        "answer_scale": 1.96,
        "answer_scale_label": "原本指定の196%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(150, 570, 515, 785),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(60, 355, 910, 765), "ref_size": [1019, 1517]},
        ],
        "explanation": [
            {"page": 7, "box": box(105, 340, 965, 970), "ref_size": [1020, 1518]},
        ],
    },
    {
        "slug": "hokkaido_q5_2023_math",
        "year": 2023,
        "grade": 1,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 5,
        "field": "データの活用",
        "filename": "2023年実施_北海道_中1数学_度数分布と相対度数（累積度数・度数折れ線・分布の比較）.pdf",
        "stamp": "度数分布と相対度数 - 累積度数、度数折れ線、分布の比較",
        "science_ref": [1023, 1517],
        "problem": [
            {"page": 6, "box": box(75, 365, 910, 1390)},
            {"page": 7, "box": box(135, 145, 945, 1380), "ref_size": [1019, 1519]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(520, 760, 865, 1335),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(65, 355, 915, 1070), "ref_size": [1024, 1517]},
        ],
        "explanation": [
            {"page": 11, "box": box(105, 220, 960, 635), "ref_size": [1022, 1518]},
        ],
    },
]
