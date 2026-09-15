"""長野県 2017〜2021年・数学 採用10題（150 dpi基準）の測定結果。"""

CONFIGS = [
    {
        "slug": "nagano_2018_q3",
        "repo": "koukou-nyushi-nagano",
        "year": 2018,
        "prefecture": "長野県",
        "question": 3,
        "question_label": "問3",
        "grade": 2,
        "field": "関数",
        "filename": "2018年実施_長野県_中2数学_一次関数とダイヤグラム（2台のエレベーターの動き）.pdf",
        "stamp": "一次関数とダイヤグラム（2台のエレベーターの動き）",
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 5, "box": [120, 135, 970, 1310]},
            {"page": 6, "box": [120, 145, 970, 1340]},
        ],
        "problem_page_groups": [[1], [2]],
        "problem_scale_cap": 0.99,
        "answer_scale": 1.94,
        "answer_scale_label": "原本指定の194%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [120, 745, 500, 1370],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 9, "box": [90, 355, 970, 750]},
        ],
        "explanation": [
            {"page": 11, "box": [90, 670, 970, 1460]},
            {"page": 12, "box": [90, 155, 970, 205]},
        ],
    },
    {
        "slug": "nagano_2019_q3",
        "repo": "koukou-nyushi-nagano",
        "year": 2019,
        "prefecture": "長野県",
        "question": 3,
        "question_label": "問3",
        "grade": 2,
        "field": "関数",
        "filename": "2019年実施_長野県_中2数学_一次関数のグラフの利用（プールの排水とポンプ）.pdf",
        "stamp": "一次関数のグラフの利用（プールの排水とポンプ）",
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 4, "box": [95, 805, 970, 1410]},
            {"page": 5, "box": [115, 135, 970, 1370]},
            {"page": 6, "box": [105, 145, 970, 730]},
        ],
        "problem_scale_cap": 0.99,
        "answer_scale": 1.85,
        "answer_scale_label": "原本指定の185%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [105, 740, 550, 1380],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 8, "box": [90, 355, 970, 750]},
        ],
        "explanation": [
            {"page": 9, "box": [90, 1338, 970, 1465]},
            {"page": 10, "box": [90, 165, 970, 965]},
        ],
    },
    {
        "slug": "nagano_2020_q3",
        "repo": "koukou-nyushi-nagano",
        "year": 2020,
        "prefecture": "長野県",
        "question": 3,
        "question_label": "問3",
        "grade": 2,
        "field": "関数",
        "filename": "2020年実施_長野県_中2数学_一次関数のグラフの読み取りと利用（2店のリボンの値段）.pdf",
        "stamp": "一次関数のグラフの読み取りと利用（2店のリボンの値段）",
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 5, "box": [110, 135, 970, 1410]},
            {"page": 6, "box": [105, 145, 970, 1390]},
        ],
        "problem_page_groups": [[1], [2]],
        "problem_scale_cap": 0.95,
        "answer_scale": 1.92,
        "answer_scale_label": "原本指定の192%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [115, 755, 490, 1280],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 9, "box": [90, 353, 970, 752]},
        ],
        "explanation": [
            {"page": 10, "box": [90, 1098, 970, 1440]},
            {"page": 11, "box": [90, 168, 970, 612]},
        ],
    },
    # 問題p5-6、正解p9、解説p11、解答用紙p1。
    # Iは一次関数、IIは二乗に比例する関数と一次関数の複合大問。
    {
        "slug": "nagano_2017_q3",
        "repo": "koukou-nyushi-nagano",
        "year": 2017,
        "prefecture": "長野県",
        "question": 3,
        "question_label": "問3",
        "grade": 3,
        "field": "関数",
        "detail_unit": (
            "二乗に比例する関数と一次関数の総合"
            "（移動グラフ・放物線・面積）"
        ),
        "filename": (
            "2017年実施_長野県_中3数学_"
            "二乗に比例する関数と一次関数の総合"
            "（移動グラフ・放物線・面積）.pdf"
        ),
        "stamp": (
            "二乗に比例する関数と一次関数の総合 - "
            "移動グラフ、放物線、面積"
        ),
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 5, "box": [105, 130, 970, 1415]},
            {"page": 6, "box": [105, 130, 970, 1335]},
        ],
        "problem_page_groups": [[1], [2]],
        "answer_scale": 2.0,
        "answer_scale_label": (
            "原本指定の200%で配置（問3の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [115, 760, 645, 1355],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.40, 0.84, 0.56, 1.0]],
            },
        ],
        "answers": [
            {"page": 9, "box": [90, 345, 970, 760]},
        ],
        "explanation": [
            {"page": 11, "box": [90, 220, 970, 1140]},
        ],
    },
    # 問題p7-8、正解p9、解説p11-12、解答用紙p1。
    {
        "slug": "nagano_2017_q4",
        "repo": "koukou-nyushi-nagano",
        "year": 2017,
        "prefecture": "長野県",
        "question": 4,
        "question_label": "問4",
        "grade": 3,
        "field": "図形",
        "detail_unit": (
            "図形の総合（円錐・相似・円周角・三平方の定理）"
        ),
        "filename": (
            "2017年実施_長野県_中3数学_"
            "図形の総合（円錐・相似・円周角・三平方の定理）.pdf"
        ),
        "stamp": (
            "図形の総合 - 円錐、相似、円周角、三平方の定理"
        ),
        "science_ref": [1073, 1517],
        "explanation_source_pdf": r"D:\Files\(高校入試)長野県\2017(H29)年度.pdf",
        "problem": [
            {"page": 7, "box": [105, 130, 970, 1415]},
            {"page": 8, "box": [105, 130, 970, 955]},
        ],
        "problem_page_groups": [[1], [2]],
        "answer_scale": 2.0,
        "answer_scale_label": (
            "原本指定の200%で配置（問4の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [670, 760, 950, 1280],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.76, 0.78, 1.0, 1.0]],
            },
        ],
        "answers": [
            {"page": 9, "box": [90, 345, 970, 760]},
        ],
        "explanation": [
            {"page": 38, "box": [90, 1145, 970, 1465]},
            {"page": 39, "box": [90, 150, 970, 1450]},
            {"page": 40, "box": [90, 155, 1020, 270]},
        ],
    },
    # 問題p7-8、正解p9、解説p12、解答用紙p1。
    {
        "slug": "nagano_2018_q4",
        "repo": "koukou-nyushi-nagano",
        "year": 2018,
        "prefecture": "長野県",
        "question": 4,
        "question_label": "問4",
        "grade": 3,
        "field": "図形",
        "detail_unit": (
            "円周角と相似・三平方の定理"
            "（2つの円・動点・面積比）"
        ),
        "filename": (
            "2018年実施_長野県_中3数学_"
            "円周角と相似・三平方の定理"
            "（2つの円・動点・面積比）.pdf"
        ),
        "stamp": (
            "円周角と相似、三平方の定理 - 2つの円、動点、面積比"
        ),
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 7, "box": [105, 130, 970, 1415]},
            {"page": 8, "box": [105, 130, 970, 1120]},
        ],
        "problem_page_groups": [[1], [2]],
        "answer_scale": 1.94,
        "answer_scale_label": (
            "原本指定の194%で配置（問4の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [505, 760, 915, 1360],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.78, 0.69, 1.0, 1.0]],
            },
        ],
        "answers": [
            {"page": 9, "box": [90, 355, 970, 750]},
        ],
        "explanation": [
            {"page": 12, "box": [90, 210, 970, 1410]},
        ],
    },
    # 問題p6-7、正解p8、解説p10-11、解答用紙p1。
    {
        "slug": "nagano_2019_q4",
        "repo": "koukou-nyushi-nagano",
        "year": 2019,
        "prefecture": "長野県",
        "question": 4,
        "question_label": "問4",
        "grade": 3,
        "field": "図形",
        "detail_unit": (
            "相似と三平方の定理"
            "（平行四辺形・回転体・面積比）"
        ),
        "filename": (
            "2019年実施_長野県_中3数学_"
            "相似と三平方の定理"
            "（平行四辺形・回転体・面積比）.pdf"
        ),
        "stamp": (
            "相似と三平方の定理 - 平行四辺形、回転体、面積比"
        ),
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 6, "box": [105, 735, 970, 1415]},
            {"page": 7, "box": [105, 130, 970, 650]},
        ],
        "answer_scale": 1.85,
        "answer_scale_label": (
            "原本指定の185%で配置（問4の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [605, 760, 970, 1310],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.765, 0.825, 1.0, 1.0]],
            },
        ],
        "answers": [
            {"page": 8, "box": [90, 355, 970, 750]},
        ],
        "explanation": [
            {"page": 10, "box": [90, 960, 970, 1465]},
            {"page": 11, "box": [90, 150, 1010, 575]},
        ],
    },
    # 問題p7-8、正解p9、解説p11-12、解答用紙p1。
    {
        "slug": "nagano_2020_q4",
        "repo": "koukou-nyushi-nagano",
        "year": 2020,
        "prefecture": "長野県",
        "question": 4,
        "question_label": "問4",
        "grade": 3,
        "field": "図形",
        "detail_unit": (
            "円周角と相似・三平方の定理"
            "（2つの円・動点・面積比）"
        ),
        "filename": (
            "2020年実施_長野県_中3数学_"
            "円周角と相似・三平方の定理"
            "（2つの円・動点・面積比）.pdf"
        ),
        "stamp": (
            "円周角と相似、三平方の定理 - 2つの円、動点、面積比"
        ),
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 7, "box": [105, 130, 970, 1415]},
            {"page": 8, "box": [105, 130, 970, 1000]},
        ],
        "problem_page_groups": [[1], [2]],
        "answer_scale": 1.92,
        "answer_scale_label": (
            "原本指定の192%で配置（問4の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [545, 760, 955, 1350],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.79, 0.72, 1.0, 1.0]],
            },
        ],
        "answers": [
            {"page": 9, "box": [90, 353, 970, 752]},
        ],
        "explanation": [
            {"page": 11, "box": [90, 605, 1020, 1465]},
            {"page": 12, "box": [90, 150, 1020, 490]},
        ],
    },
    # 問題p6-7、正解p10、解説p11-12、解答用紙p1。
    {
        "slug": "nagano_2021_q3",
        "repo": "koukou-nyushi-nagano",
        "year": 2021,
        "prefecture": "長野県",
        "question": 3,
        "question_label": "問3",
        "grade": 3,
        "field": "関数",
        "detail_unit": (
            "二乗に比例する関数と一次関数"
            "（徒歩・自転車・電車・自動車）"
        ),
        "filename": (
            "2021年実施_長野県_中3数学_"
            "二乗に比例する関数と一次関数"
            "（徒歩・自転車・電車・自動車）.pdf"
        ),
        "stamp": (
            "二乗に比例する関数と一次関数 - 徒歩、自転車、電車、自動車"
        ),
        "science_ref": [1073, 1517],
        "problem": [
            {"page": 6, "box": [105, 130, 970, 1415]},
            {"page": 7, "box": [105, 130, 970, 885]},
        ],
        "problem_page_groups": [[1], [2]],
        "answer_scale": 1.89,
        "answer_scale_label": (
            "原本指定の189%で配置（問3の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [110, 760, 540, 1380],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.18, 0.87, 0.38, 1.0]],
            },
        ],
        "answers": [
            {"page": 10, "box": [90, 345, 970, 770]},
        ],
        "explanation": [
            {"page": 11, "box": [90, 1205, 970, 1465]},
            {
                "page": 12,
                "box": [90, 160, 970, 1010],
                "white_masks": [[0.0, 0.90, 0.73, 1.0]],
            },
        ],
    },
    # 問題p7-9、正解p10、解説p12、解答用紙p1。
    {
        "slug": "nagano_2021_q4",
        "repo": "koukou-nyushi-nagano",
        "year": 2021,
        "prefecture": "長野県",
        "question": 4,
        "question_label": "問4",
        "grade": 3,
        "field": "図形",
        "detail_unit": (
            "相似な図形（平行四辺形・線分比・面積比）"
        ),
        "filename": (
            "2021年実施_長野県_中3数学_"
            "相似な図形（平行四辺形・線分比・面積比）.pdf"
        ),
        "stamp": "相似な図形 - 平行四辺形、線分比、面積比",
        "science_ref": [1073, 1517],
        "explanation_source_pdf": r"D:\Files\(高校入試)長野県\2021年度.pdf",
        "problem": [
            {"page": 7, "box": [105, 895, 970, 1415]},
            {"page": 8, "box": [105, 130, 970, 1415]},
            {"page": 9, "box": [105, 130, 970, 650]},
        ],
        "problem_page_groups": [[1], [2], [3]],
        "answer_scale": 1.89,
        "answer_scale_label": (
            "原本指定の189%で配置（問4の解答欄のみ）"
        ),
        "answer_sheet": [
            {
                "page": 1,
                "box": [575, 760, 955, 1380],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
                "white_masks": [[0.58, 0.845, 1.0, 1.0]],
            },
        ],
        "answers": [
            {"page": 10, "box": [90, 345, 970, 770]},
        ],
        "explanation": [
            {
                "page": 53,
                "box": [90, 920, 970, 1450],
                "white_masks": [[0.73, 0.0, 1.0, 0.18]],
            },
            {"page": 54, "box": [90, 145, 1020, 690]},
        ],
    },
]
