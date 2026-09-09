"""徳島県 2016〜2025年・数学（150 dpi基準）の採用12題。

問題・全問正解・対象大問の解説は、Dドライブに保存された解説付き数学原本を使う。
解答欄は同じ保存場所の年度別数学解答用紙を使う。2016・2018・2019・2023年の
原本は見開き画像を含むため、各切り抜きに150 dpiでの実ページ寸法を明記した。
"""


TOKUSHIMA_ROOT = r"D:\Files\(高校入試)徳島県"


def source(filename: str) -> str:
    return rf"{TOKUSHIMA_ROOT}\{filename}"


def section_sources(problem_pdf: str, answer_pdf: str) -> dict[str, str]:
    """4セクションすべてについて、使用するDドライブ原本を明示する。"""

    return {
        "problem_source_pdf": problem_pdf,
        "answer_source_pdf": answer_pdf,
        "answers_source_pdf": problem_pdf,
        "explanation_source_pdf": problem_pdf,
    }


CONFIGS = [
    {
        "slug": "tokushima_2016_q2_math",
        "repo": "local-source-tokushima",
        "year": 2016,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 2,
        "question_label": "大問2",
        "grade": 2,
        "field": "規則性",
        "detail_unit": "かけ算九九表の規則性（横に並ぶ3数・文字式による説明・倍数）",
        "filename": "2016年実施_徳島県_中2数学_かけ算九九表の規則性（横に並ぶ3数・文字式による説明・倍数）.pdf",
        "stamp": "かけ算九九表の規則性（横に並ぶ3数・文字式による説明・倍数）",
        **section_sources(
            source("2016(H28)_数学.pdf"),
            source("2016(H28)_数学解答用紙.pdf"),
        ),
        "science_ref": [2148, 1517],
        "science_dpi": 1000,
        "problem": [
            {"page": 2, "box": [1040, 410, 2140, 1405], "ref_size": [2148, 1517]},
        ],
        "answer_scale": 1.60,
        "answer_scale_label": "原本指定の160%で配置（大問2の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [155, 675, 600, 930],
                "source_ref_size": [2148, 1517],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 5, "box": [1130, 315, 2120, 620], "ref_size": [2148, 1517]},
        ],
        "explanation": [
            {"page": 6, "box": [120, 270, 790, 500], "ref_size": [2148, 1517]},
            {"page": 6, "box": [120, 500, 1025, 715], "ref_size": [2148, 1517]},
        ],
    },
    {
        "slug": "tokushima_2016_q5_math",
        "repo": "local-source-tokushima",
        "year": 2016,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 5,
        "question_label": "大問5",
        "grade": 2,
        "field": "方程式の利用",
        "detail_unit": "連立方程式の応用（駐車区画・小型車と大型車・長さの測定）",
        "filename": "2016年実施_徳島県_中2数学_連立方程式の応用（駐車区画・小型車と大型車・長さの測定）.pdf",
        "stamp": "連立方程式の応用（駐車区画・小型車と大型車・長さの測定）",
        **section_sources(
            source("2016(H28)_数学.pdf"),
            source("2016(H28)_数学解答用紙.pdf"),
        ),
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [120, 1020, 1030, 1300], "ref_size": [2148, 1517]},
            {"page": 3, "box": [1040, 100, 2135, 860], "ref_size": [2148, 1517]},
        ],
        "answer_scale": 1.60,
        "answer_scale_label": "原本指定の160%で配置（大問5の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [600, 720, 1025, 1330],
                "source_ref_size": [2148, 1517],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 5, "box": [1130, 315, 2120, 620], "ref_size": [2148, 1517]},
        ],
        "explanation": [
            {"page": 6, "box": [1035, 585, 2135, 1020], "ref_size": [2148, 1517]},
        ],
    },
    {
        "slug": "tokushima_2018_q5_math",
        "repo": "local-source-tokushima",
        "year": 2018,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 5,
        "question_label": "大問5",
        "grade": 2,
        "field": "方程式の利用",
        "detail_unit": "連立方程式の応用（遊園地の移動時間・待ち時間・観覧車）",
        "filename": "2018年実施_徳島県_中2数学_連立方程式の応用（遊園地の移動時間・待ち時間・観覧車）.pdf",
        "stamp": "連立方程式の応用（遊園地の移動時間・待ち時間・観覧車）",
        **section_sources(
            source("2018(H30) _数学.pdf"),
            source("2018(H30) _数学解答用紙.pdf"),
        ),
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [1040, 610, 2135, 1320], "ref_size": [2148, 1517]},
            {"page": 5, "box": [110, 100, 1030, 600], "ref_size": [2148, 1517]},
        ],
        "answer_scale": 1.73,
        "answer_scale_label": "原本指定の173%で配置（大問5の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [1600, 665, 2010, 1210],
                "source_ref_size": [2148, 1517],
                "rotation": 0,
                "white_masks": [[0.0, 0.25, 0.17, 1.0]],
            },
        ],
        "answers": [
            {"page": 6, "box": [1160, 320, 2060, 650], "ref_size": [2148, 1517]},
        ],
        "explanation": [
            {"page": 8, "box": [1050, 560, 2135, 1120], "ref_size": [2148, 1517]},
        ],
    },
    {
        "slug": "tokushima_2019_q3_math",
        "repo": "local-source-tokushima",
        "year": 2019,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 3,
        "question_label": "大問3",
        "grade": 2,
        "field": "関数",
        "detail_unit": "一次関数と連立方程式の応用（高度と気温・チェアリフト）",
        "filename": "2019年実施_徳島県_中2数学_一次関数と連立方程式の応用（高度と気温・チェアリフト）.pdf",
        "stamp": "一次関数と連立方程式の応用（高度と気温・チェアリフト）",
        **section_sources(
            source("2019数学.pdf"),
            source("2019数学_解答用紙.pdf"),
        ),
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [120, 150, 1035, 1230], "ref_size": [2148, 1517]},
        ],
        "answer_scale": 1.59,
        "answer_scale_label": "原本指定の159%で配置（大問3の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [105, 920, 480, 1270],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": [1160, 330, 2070, 790], "ref_size": [2148, 1517]},
        ],
        "explanation": [
            {"page": 7, "box": [120, 1275, 1035, 1450], "ref_size": [2148, 1517]},
            {"page": 7, "box": [1110, 150, 2125, 590], "ref_size": [2148, 1517]},
        ],
    },
    {
        "slug": "tokushima_2021_q2_math",
        "repo": "local-source-tokushima",
        "year": 2021,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 2,
        "question_label": "大問2",
        "grade": 2,
        "field": "方程式の利用",
        "detail_unit": "連立方程式の応用（玉ねぎとじゃがいもの袋数・個数・売上）",
        "filename": "2021年実施_徳島県_中2数学_連立方程式の応用（玉ねぎとじゃがいもの袋数・個数・売上）.pdf",
        "stamp": "連立方程式の応用（玉ねぎとじゃがいもの袋数・個数・売上）",
        **section_sources(
            source("2021_数学.pdf"),
            source("2021_数学解答用紙.pdf"),
        ),
        "science_ref": [1024, 1527],
        "problem": [
            {"page": 2, "box": [90, 650, 980, 1390], "ref_size": [1024, 1527]},
            {"page": 3, "box": [90, 120, 970, 440], "ref_size": [1024, 1525]},
        ],
        "answer_scale": 1.54,
        "answer_scale_label": "原本指定の154%で配置（大問2の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [90, 820, 535, 1110],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": [60, 340, 930, 670], "ref_size": [1028, 1523]},
        ],
        "explanation": [
            {"page": 7, "box": [90, 480, 980, 1120], "ref_size": [1027, 1524]},
        ],
    },
    {
        "slug": "tokushima_2022_q3_math",
        "repo": "local-source-tokushima",
        "year": 2022,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 3,
        "question_label": "大問3",
        "grade": 2,
        "field": "関数",
        "detail_unit": "一次関数のグラフの利用（Tシャツ注文料金・3社の比較）",
        "filename": "2022年実施_徳島県_中2数学_一次関数のグラフの利用（Tシャツ注文料金・3社の比較）.pdf",
        "stamp": "一次関数のグラフの利用（Tシャツ注文料金・3社の比較）",
        **section_sources(
            source("2022_数学.pdf"),
            source("2022_数学解答用紙.pdf"),
        ),
        "science_ref": [1023, 1526],
        "problem": [
            {"page": 2, "box": [85, 1000, 970, 1425], "ref_size": [1023, 1526]},
            {"page": 3, "box": [90, 130, 970, 1430], "ref_size": [1023, 1527]},
            {"page": 4, "box": [90, 140, 950, 785], "ref_size": [1022, 1526]},
        ],
        "answer_scale": 1.61,
        "answer_scale_label": "原本指定の161%で配置（大問3の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [500, 320, 955, 600],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": [65, 340, 930, 750], "ref_size": [1022, 1522]},
        ],
        "explanation": [
            {"page": 7, "box": [90, 1080, 970, 1445], "ref_size": [1022, 1525]},
            {"page": 8, "box": [90, 150, 970, 480], "ref_size": [1021, 1523]},
        ],
    },
    {
        "slug": "tokushima_2023_q3_math",
        "repo": "local-source-tokushima",
        "year": 2023,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 3,
        "question_label": "大問3",
        "grade": 1,
        "field": "データの活用",
        "detail_unit": "資料の散らばりと代表値（ヒストグラム・最頻値・相対度数・累積相対度数・中央値）",
        "filename": "2023年実施_徳島県_中1数学_資料の散らばりと代表値（ヒストグラム・最頻値・相対度数・累積相対度数・中央値）.pdf",
        "stamp": "資料の散らばりと代表値（ヒストグラム・最頻値・相対度数・累積相対度数・中央値）",
        **section_sources(
            source("2023_数学.pdf"),
            source("2023_数学_解答用紙.pdf"),
        ),
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 2, "box": [1070, 580, 2135, 1380], "ref_size": [2148, 1517]},
            {"page": 3, "box": [120, 120, 1035, 1380], "ref_size": [2148, 1517]},
            {"page": 3, "box": [1070, 120, 2135, 590], "ref_size": [2148, 1517]},
        ],
        "answer_scale": 1.61,
        "answer_scale_label": "原本指定の161%で配置（大問3の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [110, 980, 530, 1380],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": [1170, 330, 2040, 660], "ref_size": [2148, 1517]},
        ],
        "explanation": [
            {"page": 7, "box": [120, 1160, 1035, 1450], "ref_size": [2148, 1517]},
            {"page": 7, "box": [1070, 150, 2135, 370], "ref_size": [2148, 1517]},
        ],
    },
    {
        "slug": "tokushima_2023_q4_math",
        "repo": "local-source-tokushima",
        "year": 2023,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "方程式の利用",
        "detail_unit": "方程式と文字式の応用（文化祭の時間配分・発表グループ数）",
        "filename": "2023年実施_徳島県_中2数学_方程式と文字式の応用（文化祭の時間配分・発表グループ数）.pdf",
        "stamp": "方程式と文字式の応用（文化祭の時間配分・発表グループ数）",
        **section_sources(
            source("2023_数学.pdf"),
            source("2023_数学_解答用紙.pdf"),
        ),
        "science_ref": [2148, 1517],
        "problem": [
            {"page": 3, "box": [1035, 600, 2135, 1420], "ref_size": [2148, 1517]},
            {"page": 5, "box": [120, 120, 1035, 670], "ref_size": [2148, 1517]},
        ],
        "answer_scale": 1.61,
        "answer_scale_label": "原本指定の161%で配置（大問4の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [530, 320, 955, 560],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 6, "box": [1170, 330, 2040, 660], "ref_size": [2148, 1517]},
        ],
        "explanation": [
            {"page": 7, "box": [1035, 350, 2135, 1130], "ref_size": [2148, 1517]},
        ],
    },
    {
        "slug": "tokushima_2024_q3_math",
        "repo": "local-source-tokushima",
        "year": 2024,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 3,
        "question_label": "大問3",
        "grade": 2,
        "field": "規則性",
        "detail_unit": "マッチ棒の規則性（段数・一般式・逆向きに組み合わせたタワー）",
        "filename": "2024年実施_徳島県_中2数学_マッチ棒の規則性（段数・一般式・逆向きに組み合わせたタワー）.pdf",
        "stamp": "マッチ棒の規則性（段数・一般式・逆向きに組み合わせたタワー）",
        **section_sources(
            source("2024_数学.pdf"),
            source("2024_数学解答用紙.pdf"),
        ),
        "science_ref": [1027, 1522],
        "problem": [
            {"page": 3, "box": [100, 185, 975, 1335], "ref_size": [1027, 1522]},
            {"page": 4, "box": [100, 130, 965, 1290], "ref_size": [1025, 1520]},
        ],
        "answer_scale": 1.54,
        "answer_scale_label": "原本指定の154%で配置（大問3の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [90, 1200, 520, 1400],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": [55, 350, 930, 675], "ref_size": [1022, 1520]},
        ],
        "explanation": [
            {"page": 8, "box": [90, 790, 970, 1430], "ref_size": [1022, 1522]},
        ],
    },
    {
        "slug": "tokushima_2024_q4_math",
        "repo": "local-source-tokushima",
        "year": 2024,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 4,
        "question_label": "大問4",
        "grade": 2,
        "field": "関数",
        "detail_unit": "一次関数と図形の応用（座標・正方形・回転体・最短経路）",
        "filename": "2024年実施_徳島県_中2数学_一次関数と図形の応用（座標・正方形・回転体・最短経路）.pdf",
        "stamp": "一次関数と図形の応用（座標・正方形・回転体・最短経路）",
        **section_sources(
            source("2024_数学.pdf"),
            source("2024_数学解答用紙.pdf"),
        ),
        "science_ref": [1025, 1520],
        "problem": [
            {"page": 4, "box": [90, 1305, 980, 1395], "ref_size": [1025, 1520]},
            {"page": 5, "box": [100, 140, 975, 850], "ref_size": [1027, 1522]},
        ],
        "answer_scale": 1.54,
        "answer_scale_label": "原本指定の154%で配置（大問4の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [535, 290, 980, 490],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": [55, 350, 930, 675], "ref_size": [1022, 1520]},
        ],
        "explanation": [
            {"page": 9, "box": [70, 150, 970, 840], "ref_size": [1022, 1520]},
        ],
    },
    {
        "slug": "tokushima_2025_q2_math",
        "repo": "local-source-tokushima",
        "year": 2025,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 2,
        "question_label": "大問2",
        "grade": 2,
        "field": "方程式の利用",
        "detail_unit": "連立方程式の応用（運動時間・身体活動量・道のりと速さ）",
        "filename": "2025年実施_徳島県_中2数学_連立方程式の応用（運動時間・身体活動量・道のりと速さ）.pdf",
        "stamp": "連立方程式の応用（運動時間・身体活動量・道のりと速さ）",
        **section_sources(
            source("2025_徳島県_数学.pdf"),
            source("2025_数学解答用紙.pdf"),
        ),
        "science_ref": [1040, 1519],
        "problem": [
            {"page": 2, "box": [85, 480, 980, 1390], "ref_size": [1040, 1519]},
            {"page": 3, "box": [90, 120, 970, 300], "ref_size": [1041, 1520]},
        ],
        "answer_scale": 1.59,
        "answer_scale_label": "原本指定の159%で配置（大問2の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [100, 760, 530, 910],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": [70, 350, 930, 710], "ref_size": [1033, 1517]},
        ],
        "explanation": [
            {"page": 8, "box": [90, 690, 980, 1130], "ref_size": [1034, 1517]},
        ],
    },
    {
        "slug": "tokushima_2025_q3_math",
        "repo": "local-source-tokushima",
        "year": 2025,
        "session": "一般選抜",
        "prefecture": "徳島県",
        "question": 3,
        "question_label": "大問3",
        "grade": 2,
        "field": "規則性",
        "detail_unit": "時計の規則性（LED表示・場合の数・時計の針・一次方程式・作図）",
        "filename": "2025年実施_徳島県_中2数学_時計の規則性（LED表示・場合の数・時計の針・一次方程式・作図）.pdf",
        "stamp": "時計の規則性（LED表示・場合の数・時計の針・一次方程式・作図）",
        **section_sources(
            source("2025_徳島県_数学.pdf"),
            source("2025_数学解答用紙.pdf"),
        ),
        "science_ref": [1041, 1520],
        "problem": [
            {"page": 3, "box": [90, 310, 975, 1380], "ref_size": [1041, 1520]},
            {"page": 4, "box": [90, 120, 970, 1270], "ref_size": [1040, 1518]},
        ],
        "answer_scale": 1.59,
        "answer_scale_label": "原本指定の159%で配置（大問3の解答欄のみ）",
        "answer_sheet": [
            {
                "page": 1,
                "box": [100, 930, 595, 1400],
                "source_ref_size": [1075, 1518],
                "rotation": 0,
            },
        ],
        "answers": [
            {"page": 7, "box": [70, 350, 930, 710], "ref_size": [1033, 1517]},
        ],
        "explanation": [
            {"page": 8, "box": [90, 1160, 980, 1440], "ref_size": [1034, 1517]},
            {"page": 9, "box": [90, 155, 980, 350], "ref_size": [1031, 1517]},
        ],
    },
]
