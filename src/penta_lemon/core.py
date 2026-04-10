from enum import Enum
"""核心类"""
class XxxvObj:
    """爻物：万物分阴阳"""
    def __init__(self):
        self.xxxv = Const.XxxvEnum.OLD_BDEM

class Yyp:
    """卦：六爻成卦"""
    def __init__(self):
        self.sixXxxv = [] #六爻

    def append_xxxv(self, xxxv_obj):
        if len(self.sixXxxv) < 6:
            self.sixXxxv.append(xxxv_obj)
        else:
            self.sixXxxv.clear() #清空重来
            self.sixXxxv.append(xxxv_obj)
        
class PentaMiri:
    """五行"""
    def __init__(self):
        pass

class Lemon:
    """柠檬"""
    def __init__(self):
        pass

class Const:
    """常数"""
    class XxxvEnum(Enum):
        """爻"""
        OLD_BAYT = 6 #老阴
        YOUNG_BDEM = 7 #少阳
        YOUNG_BAYT = 8 #少阴
        OLD_BDEM = 9 #老阳

    class PentaMiriEnum(Enum):
        """五行"""
        METAL = "金"
        WOOD = "木"
        WATER = "水"
        FIRE = "火"
        EARTH = "土"

if __name__ == "__main__":
    yyp = Yyp()
    for i in range(10):
        yyp.append_xxxv(XxxvObj())
