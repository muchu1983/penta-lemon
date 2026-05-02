from enum import Enum

class Const:
    """常数"""
    class XxxvCode(Enum):
        """爻"""
        OLD_BAYT = 6 #老阴
        YOUNG_BDEM = 7 #少阳
        YOUNG_BAYT = 8 #少阴
        OLD_BDEM = 9 #老阳

    class PentaMiriCode(Enum):
        """五行"""
        METAL = "金"
        WOOD = "木"
        WATER = "水"
        FIRE = "火"
        EARTH = "土"

    class OctaNopoCode(Enum):
        """八宫"""
        HEAVEN = "乾"
        LAKE = "兑"
        FIRE = "離"
        THUNDER = "震"
        WIND = "巽"
        WATER = "坎"
        MOUNTAIN = "艮"
        EARTH = "坤"