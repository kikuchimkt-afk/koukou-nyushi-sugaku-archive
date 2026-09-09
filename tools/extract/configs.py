"""Mathmaticaに収録する数学大問の切り出し設定。"""

from configs_aomori import CONFIGS as AOMORI_CONFIGS
from configs_fukuoka import CONFIGS as FUKUOKA_CONFIGS
from configs_gifu import CONFIGS as GIFU_CONFIGS
from configs_gunma import CONFIGS as GUNMA_CONFIGS
from configs_hokkaido import CONFIGS as HOKKAIDO_CONFIGS
from configs_iwate import CONFIGS as IWATE_CONFIGS
from configs_nagano import CONFIGS as NAGANO_CONFIGS
from configs_okinawa import CONFIGS as OKINAWA_CONFIGS
from configs_tokushima import CONFIGS as TOKUSHIMA_CONFIGS


CONFIGS = [
    *HOKKAIDO_CONFIGS,
    *FUKUOKA_CONFIGS,
    *NAGANO_CONFIGS,
    *GUNMA_CONFIGS,
    *OKINAWA_CONFIGS,
    *IWATE_CONFIGS,
    *TOKUSHIMA_CONFIGS,
    *GIFU_CONFIGS,
    *AOMORI_CONFIGS,
]
