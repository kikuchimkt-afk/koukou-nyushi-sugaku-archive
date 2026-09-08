"""Mathmaticaに収録する数学大問の切り出し設定。"""

from configs_fukuoka import CONFIGS as FUKUOKA_CONFIGS
from configs_hokkaido import CONFIGS as HOKKAIDO_CONFIGS
from configs_nagano import CONFIGS as NAGANO_CONFIGS


CONFIGS = [
    *HOKKAIDO_CONFIGS,
    *FUKUOKA_CONFIGS,
    *NAGANO_CONFIGS,
]
