"""生成履歴に記録するPDFパイプラインの版を定義する。"""

from __future__ import annotations

import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
PIPELINE_FILES = (
    HERE / "base_builder.py",
    HERE / "build_math.py",
    HERE / "source_paths.py",
    Path(__file__).resolve(),
)

# 2026-09-08に現行のローカル基底で再生成・監査済みの22題。
# 当時のmanifestにはpipelineSha256が無いため、基底ハッシュと個別設定・
# 原本・PDFハッシュによる従来監査を明示的に継続する。再生成した項目には
# 現行pipelineSha256が記録され、この例外は使われなくなる。
LEGACY_PIPELINE_SLUGS = frozenset(
    {
        "hokkaido_q3_2018_math",
        "hokkaido_q3_2019_math",
        "hokkaido_q5_2019_math",
        "hokkaido_q3_2020_math",
        "hokkaido_q3_2021_math",
        "hokkaido_q5_2021_math",
        "hokkaido_q2_2022_math",
        "hokkaido_q5_2023_math",
        "fukuoka_q2_2017",
        "fukuoka_q4_2017",
        "fukuoka_q3_2018",
        "fukuoka_q4_2018",
        "fukuoka_q2_2019",
        "fukuoka_q3_2019",
        "fukuoka_q4_2019",
        "fukuoka_q3_2020",
        "fukuoka_q4_2020",
        "fukuoka_q2_2021",
        "fukuoka_q4_2021",
        "nagano_2018_q3",
        "nagano_2019_q3",
        "nagano_2020_q3",
    }
)


def pipeline_sha256() -> str:
    digest = hashlib.sha256()
    for path in PIPELINE_FILES:
        digest.update(path.name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()
