"""北海道・数学 採用20題の150dpi基準切り出し設定。

元PDFはすべて koukou-nyushi-hokkaido/public/files/{year}/ 配下。
このファイルは測定結果の引き渡し用で、数学アプリ本体には未適用。

中3再監査では共通・通常問題13題を採用し、既存1題を最高学年へ
再分類したうえで12題を追加した。学校裁量問題3題は未収録。
"""


def box(x1: int, y1: int, x2: int, y2: int) -> list[int]:
    return [x1, y1, x2, y2]


CONFIGS = [
    {
        "slug": "hokkaido_q3_2018_math",
        "year": 2018,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "データの活用",
        "filename": "2018年実施_北海道_中3数学_標本調査（無作為抽出・相対度数・中央値による母集団の比較）.pdf",
        "stamp": "標本調査 - 無作為抽出、相対度数、中央値、母集団の比較",
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
    {
        "slug": "hokkaido_q4_2018_math",
        "year": 2018,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 4,
        "field": "関数",
        "filename": "2018年実施_北海道_中3数学_二次関数の利用（変域・直線の傾き・三角形の面積）.pdf",
        "stamp": "二次関数の利用 - 変域、直線の傾き、三角形の面積",
        "science_ref": [1075, 1518],
        "problem": [
            {"page": 3, "box": box(105, 1190, 970, 1335)},
            {"page": 4, "box": box(105, 115, 970, 560)},
        ],
        "answer_scale": 1.68,
        "answer_scale_label": "原本指定の168%で配置（通常問題Q4の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(535, 365, 890, 720),
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
            {"page": 6, "box": box(105, 1010, 970, 1295)},
        ],
    },
    {
        "slug": "hokkaido_q5_2018_math",
        "year": 2018,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 5,
        "field": "図形の証明",
        "filename": "2018年実施_北海道_中3数学_円と相似の証明（円周角・中点連結定理・平行線）.pdf",
        "stamp": "円と相似の証明 - 円周角、中点連結定理、平行線",
        "science_ref": [1075, 1518],
        # p4上部の通常問題Q5だけ。直後の黒帯「学校裁量問題」は含めない。
        "problem": [
            {"page": 4, "box": box(105, 550, 970, 920)},
        ],
        "answer_scale": 1.68,
        "answer_scale_label": "原本指定の168%で配置（通常問題Q5の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(535, 715, 890, 1095),
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
            {"page": 6, "box": box(105, 1300, 970, 1508)},
            {"page": 7, "box": box(105, 150, 970, 275)},
        ],
    },
    {
        "slug": "hokkaido_q4_2019_math",
        "year": 2019,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 4,
        "field": "関数",
        "filename": "2019年実施_北海道_中3数学_二次関数の利用（対称な点・直線の傾き・直角二等辺三角形）.pdf",
        "stamp": "二次関数の利用 - 対称な点、直線の傾き、直角二等辺三角形",
        "science_ref": [1024, 1520],
        "problem": [
            {"page": 3, "box": box(75, 610, 940, 1360)},
        ],
        "answer_scale": 1.67,
        "answer_scale_label": "原本指定の167%で配置（通常問題Q4の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(535, 430, 890, 755),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(65, 365, 925, 835), "ref_size": [1025, 1518]},
        ],
        "explanation": [
            {"page": 7, "box": box(105, 1220, 965, 1505), "ref_size": [1025, 1520]},
            {"page": 8, "box": box(65, 150, 950, 335), "ref_size": [1024, 1518]},
        ],
    },
    {
        "slug": "hokkaido_q4_2020_math",
        "year": 2020,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 4,
        "field": "関数",
        "filename": "2020年実施_北海道_中3数学_二次関数の利用（放物線の対称性・直線の式・変化の割合）.pdf",
        "stamp": "二次関数の利用 - 放物線の対称性、直線の式、変化の割合",
        "science_ref": [1019, 1523],
        "problem": [
            {"page": 4, "box": box(60, 690, 955, 1490), "ref_size": [1018, 1521]},
        ],
        "answer_scale": 1.67,
        "answer_scale_label": "原本指定の167%で配置（通常問題Q4の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(530, 350, 890, 730),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": box(60, 360, 915, 985), "ref_size": [1020, 1521]},
        ],
        "explanation": [
            {"page": 9, "box": box(60, 305, 965, 660), "ref_size": [1021, 1520]},
        ],
    },
    {
        "slug": "hokkaido_q5_2020_math",
        "year": 2020,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 5,
        "field": "図形の証明",
        "filename": "2020年実施_北海道_中3数学_円と相似の証明（円周角の定理の逆・相似条件）.pdf",
        "stamp": "円と相似の証明 - 円周角の定理の逆、相似条件",
        "science_ref": [1019, 1523],
        # p5上部の通常問題Q5だけ。直後の黒帯「学校裁量問題」は含めない。
        "problem": [
            {"page": 5, "box": box(75, 135, 930, 490)},
        ],
        "answer_scale": 1.67,
        "answer_scale_label": "原本指定の167%で配置（通常問題Q5の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(530, 730, 890, 1155),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": box(60, 360, 915, 985), "ref_size": [1020, 1521]},
        ],
        "explanation": [
            {"page": 9, "box": box(60, 665, 965, 910), "ref_size": [1021, 1520]},
        ],
    },
    {
        "slug": "hokkaido_q4_2021_math",
        "year": 2021,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 4,
        "field": "関数",
        "filename": "2021年実施_北海道_中3数学_二次関数の利用（対称なグラフ・変域・距離の最小）.pdf",
        "stamp": "二次関数の利用 - 対称なグラフ、変域、距離の最小",
        "science_ref": [1021, 1519],
        "problem": [
            {"page": 4, "box": box(115, 590, 930, 1495), "ref_size": [1018, 1521]},
        ],
        "answer_scale": 1.59,
        "answer_scale_label": "原本指定の159%で配置（通常問題Q4の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(540, 480, 905, 880),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(60, 355, 915, 950), "ref_size": [1021, 1517]},
        ],
        "explanation": [
            {"page": 10, "box": box(60, 690, 955, 1290), "ref_size": [1021, 1517]},
        ],
    },
    {
        "slug": "hokkaido_q3_2022_math",
        "year": 2022,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "関数",
        "filename": "2022年実施_北海道_中3数学_二次関数の利用（放物線の性質・積が一定・説明）.pdf",
        "stamp": "二次関数の利用 - 放物線の性質、積が一定、説明",
        "science_ref": [1021, 1518],
        "problem": [
            {"page": 3, "box": box(105, 480, 950, 1500), "ref_size": [1020, 1520]},
            {"page": 4, "box": box(105, 140, 950, 645), "ref_size": [1022, 1521]},
        ],
        "answer_scale": 1.96,
        "answer_scale_label": "原本指定の196%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(525, 190, 875, 790),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(60, 355, 910, 765), "ref_size": [1019, 1517]},
        ],
        "explanation": [
            {"page": 7, "box": box(105, 960, 965, 1505), "ref_size": [1020, 1518]},
        ],
    },
    {
        "slug": "hokkaido_q4_2022_math",
        "year": 2022,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 4,
        "field": "図形の証明",
        "filename": "2022年実施_北海道_中3数学_円と相似の証明（円周角の定理の逆・同一円周）.pdf",
        "stamp": "円と相似の証明 - 円周角の定理の逆、同一円周",
        "science_ref": [1021, 1518],
        "problem": [
            {"page": 4, "box": box(60, 650, 950, 1500), "ref_size": [1022, 1521]},
        ],
        "answer_scale": 1.96,
        "answer_scale_label": "原本指定の196%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(155, 805, 510, 1405),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(60, 355, 910, 765), "ref_size": [1019, 1517]},
        ],
        "explanation": [
            {"page": 8, "box": box(60, 160, 965, 610), "ref_size": [1018, 1516]},
        ],
    },
    {
        "slug": "hokkaido_q5_2022_math",
        "year": 2022,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 5,
        "field": "数と式",
        "filename": "2022年実施_北海道_中3数学_平方根と図形の利用（三平方の定理・相似・確率）.pdf",
        "stamp": "平方根と図形の利用 - 三平方の定理、相似、確率",
        "science_ref": [1021, 1518],
        "problem": [
            {"page": 5, "box": box(75, 135, 970, 1500)},
        ],
        "answer_scale": 1.96,
        "answer_scale_label": "原本指定の196%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(525, 805, 875, 1405),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": box(60, 355, 910, 765), "ref_size": [1019, 1517]},
        ],
        "explanation": [
            {"page": 8, "box": box(60, 610, 965, 1145), "ref_size": [1018, 1516]},
        ],
    },
    {
        "slug": "hokkaido_q2_2023_math",
        "year": 2023,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 2,
        "field": "数と式",
        "filename": "2023年実施_北海道_中3数学_展開と因数分解の利用（九九表・文字式による説明・規則性）.pdf",
        "stamp": "展開と因数分解の利用 - 九九表、文字式による説明、規則性",
        "science_ref": [1023, 1517],
        "problem": [
            {"page": 2, "box": box(75, 520, 930, 1500)},
            {"page": 3, "box": box(135, 140, 945, 1325), "ref_size": [1022, 1521]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(175, 470, 510, 740),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(65, 355, 915, 1070), "ref_size": [1024, 1517]},
        ],
        "explanation": [
            {"page": 9, "box": box(105, 860, 960, 1380), "ref_size": [1022, 1518]},
        ],
    },
    {
        "slug": "hokkaido_q3_2023_math",
        "year": 2023,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 3,
        "field": "関数",
        "filename": "2023年実施_北海道_中3数学_二次関数の利用（変化の割合・放物線と直線・面積の二等分）.pdf",
        "stamp": "二次関数の利用 - 変化の割合、放物線と直線、面積の二等分",
        "science_ref": [1023, 1517],
        "problem": [
            {"page": 4, "box": box(75, 140, 930, 1190), "ref_size": [1022, 1521]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(525, 185, 860, 735),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(65, 355, 915, 1070), "ref_size": [1024, 1517]},
        ],
        "explanation": [
            {"page": 9, "box": box(105, 1370, 960, 1505), "ref_size": [1022, 1518]},
            {"page": 10, "box": box(75, 145, 960, 725), "ref_size": [1022, 1518]},
        ],
    },
    {
        "slug": "hokkaido_q4_2023_math",
        "year": 2023,
        "grade": 3,
        "repo": "koukou-nyushi-hokkaido",
        "prefecture": "北海道",
        "question": 4,
        "field": "図形の証明",
        "filename": "2023年実施_北海道_中3数学_円と相似の証明（円周角・相似比・合同）.pdf",
        "stamp": "円と相似の証明 - 円周角、相似比、合同",
        "science_ref": [1023, 1517],
        "problem": [
            {"page": 5, "box": box(75, 135, 970, 1500)},
            {"page": 6, "box": box(105, 140, 945, 350), "ref_size": [1023, 1517]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（該当大問の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": box(170, 750, 520, 1360),
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": box(65, 355, 915, 1070), "ref_size": [1024, 1517]},
        ],
        "explanation": [
            {"page": 10, "box": box(60, 720, 960, 1505), "ref_size": [1022, 1518]},
            {"page": 11, "box": box(105, 145, 960, 210), "ref_size": [1022, 1518]},
        ],
    },
]
