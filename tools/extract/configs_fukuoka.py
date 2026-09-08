"""福岡県 2017–2021年・採用11題の切り出し設定。

座標はすべて150dpi基準。問題・正解・解説の原本は見開き画像
（2148 x 1517）、解答用紙の ``source_ref_size`` は回転前の画像
（1075 x 1518）を表す。2017–2020年の解答欄 ``box`` は clockwise
回転後の upright 座標（1518 x 1075）。
"""

CONFIGS = [
    {
        "slug": "fukuoka_q2_2017",
        "year": 2017,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 2,
        "question_label": "大問2",
        "grade": 2,
        "field": "方程式の利用",
        "filename": "2017年実施_福岡県_中2数学_連立方程式の応用（袋詰めの個数と売上金額）.pdf",
        "stamp": "連立方程式の応用 - 袋詰めの個数と売上金額",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 1, "box": [105, 1095, 1035, 1500]},
            {"page": 1, "box": [1110, 110, 2040, 475]},
        ],
        "answer_scale": 2.02,
        "answer_scale_label": "原本指定の202%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [183, 354, 640, 665],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 10, "box": [1110, 315, 2040, 650]},
        ],
        "explanation": [
            {"page": 11, "box": [105, 150, 1035, 395]},
        ],
    },
    {
        "slug": "fukuoka_q4_2017",
        "year": 2017,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "関数",
        "filename": "2017年実施_福岡県_中2数学_一次関数のグラフの利用（速さ・道のり・すれちがい）.pdf",
        "stamp": "一次関数のグラフの利用 - 速さ・道のり・すれちがい",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [1110, 110, 2040, 1205]},
        ],
        "answer_scale": 2.02,
        "answer_scale_label": "原本指定の202%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [758, 143, 1048, 278],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 10, "box": [1110, 315, 2040, 650]},
        ],
        "explanation": [
            {"page": 11, "box": [105, 575, 1035, 1195]},
        ],
    },
    {
        "slug": "fukuoka_q3_2018",
        "year": 2018,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 3,
        "question_label": "大問3",
        "grade": 1,
        "field": "データの活用",
        "filename": "2018年実施_福岡県_中1数学_相対度数と中央値（2校の読書冊数の比較）.pdf",
        "stamp": "相対度数と中央値 - 2校の読書冊数の比較",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 1, "box": [1110, 915, 2040, 1500]},
            {"page": 3, "box": [105, 105, 1035, 1265]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [206, 752, 659, 946],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 315, 2040, 680]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 565, 1035, 770]},
        ],
    },
    {
        "slug": "fukuoka_q4_2018",
        "year": 2018,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "関数",
        "filename": "2018年実施_福岡県_中2数学_一次関数のグラフの利用（水そうの水面の高さ）.pdf",
        "stamp": "一次関数のグラフの利用 - 水そうの水面の高さ",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [1110, 105, 2040, 1150]},
            {"page": 5, "box": [105, 105, 1035, 930]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [778, 144, 1262, 447],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 315, 2040, 680]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 780, 1035, 1320]},
        ],
    },
    {
        "slug": "fukuoka_q2_2019",
        "year": 2019,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 2,
        "question_label": "大問2",
        "grade": 2,
        "field": "データの活用",
        "filename": "2019年実施_福岡県_中2数学_確率（玉の取り出し・2種類のくじ引きの比較）.pdf",
        "stamp": "確率 - 玉の取り出し・2種類のくじ引きの比較",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 1, "box": [1110, 115, 2040, 945]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [222, 435, 674, 772],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 750]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 310, 1035, 580]},
        ],
    },
    {
        "slug": "fukuoka_q3_2019",
        "year": 2019,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 3,
        "question_label": "大問3",
        "grade": 2,
        "field": "数と式",
        "filename": "2019年実施_福岡県_中2数学_式の値と等式の変形（数当てゲームの仕組みの説明）.pdf",
        "stamp": "式の値と等式の変形 - 数当てゲームの仕組みの説明",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 1, "box": [1110, 950, 2040, 1500]},
            {"page": 3, "box": [105, 105, 1035, 1500]},
            {"page": 3, "box": [1110, 105, 2040, 305]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [222, 772, 674, 946],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 750]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 590, 1035, 810]},
        ],
    },
    {
        "slug": "fukuoka_q4_2019",
        "year": 2019,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "関数",
        "filename": "2019年実施_福岡県_中2数学_一次関数のグラフの利用（通学の道のりと時間）.pdf",
        "stamp": "一次関数のグラフの利用 - 通学の道のりと時間",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [1110, 315, 2040, 1500]},
            {"page": 5, "box": [105, 105, 1035, 1150]},
        ],
        "answer_scale": 2.00,
        "answer_scale_label": "原本指定の200%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [797, 142, 1294, 461],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 750]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 830, 1035, 1190]},
        ],
    },
    {
        "slug": "fukuoka_q3_2020",
        "year": 2020,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 3,
        "question_label": "大問3",
        "grade": 2,
        "field": "データの活用",
        "filename": "2020年実施_福岡県_中2数学_場合の数と確率（カードとコマの移動）.pdf",
        "stamp": "場合の数と確率 - カードとコマの移動",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 1, "box": [1110, 975, 2040, 1500]},
            {"page": 3, "box": [105, 105, 1035, 455]},
        ],
        "answer_scale": 1.92,
        "answer_scale_label": "原本指定の192%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [177, 531, 649, 932],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 770]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 880, 1035, 1225]},
        ],
    },
    {
        "slug": "fukuoka_q4_2020",
        "year": 2020,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "関数",
        "filename": "2020年実施_福岡県_中2数学_一次関数のグラフの利用（電話の料金プランの比較）.pdf",
        "stamp": "一次関数のグラフの利用 - 電話の料金プランの比較",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [105, 460, 1035, 1500]},
            {"page": 3, "box": [1110, 105, 2040, 1200]},
        ],
        "answer_scale": 1.92,
        "answer_scale_label": "原本指定の192%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [776, 128, 1293, 456],
                "rotation": "cw",
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 770]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 1235, 1035, 1500]},
            {"page": 9, "box": [1110, 140, 2040, 455]},
        ],
    },
    {
        "slug": "fukuoka_q2_2021",
        "year": 2021,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 2,
        "question_label": "大問2",
        "grade": 1,
        "field": "データの活用",
        "filename": "2021年実施_福岡県_中1数学_相対度数と代表値（紙飛行機の飛行距離のヒストグラム）.pdf",
        "stamp": "相対度数と代表値 - 紙飛行機の飛行距離のヒストグラム",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 2, "box": [105, 110, 1035, 1110]},
        ],
        "answer_scale": 1.28,
        "answer_scale_label": "原本指定の128%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [101, 589, 807, 909],
                "rotation": 0,
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 775]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 460, 1035, 665]},
        ],
    },
    {
        "slug": "fukuoka_q4_2021",
        "year": 2021,
        "repo": "koukou-nyushi-fukuoka",
        "prefecture": "福岡県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "関数",
        "filename": "2021年実施_福岡県_中2数学_一次関数のグラフの利用（家・図書館・駅の移動）.pdf",
        "stamp": "一次関数のグラフの利用 - 家・図書館・駅の移動",
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 4, "box": [105, 480, 1035, 1500]},
            {"page": 4, "box": [1110, 105, 2040, 665]},
        ],
        "answer_scale": 1.28,
        "answer_scale_label": "原本指定の128%で配置（解答欄は実物大相当）",
        "answer_sheet": [
            {
                "page": 2,
                "box": [88, 152, 856, 536],
                "rotation": 0,
                "source_ref_size": [1075, 1518],
            },
        ],
        "answers": [
            {"page": 8, "box": [1110, 320, 2040, 775]},
        ],
        "explanation": [
            {"page": 9, "box": [105, 1180, 1035, 1500]},
            {"page": 9, "box": [1110, 140, 2040, 540]},
        ],
    },
]
