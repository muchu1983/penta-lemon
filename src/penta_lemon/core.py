from enum import Enum
"""核心类"""
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

class XxxvObj:
    """爻物：万物分阴阳"""
    def __init__(self, xxxv:Const.XxxvEnum):
        self.xxxv = xxxv

class Yyp:
    """卦：六爻成卦"""
    def __init__(self):
        self.sixXxxv = [] #六爻

    def append_xxxv(self, xxxv_obj):
        if len(self.sixXxxv) >= 6:
            self.sixXxxv.clear() #清空重来
        self.sixXxxv.append(xxxv_obj)
    
    def isCompleted(self):
        return True if len(self.sixXxxv) == 6 else False
        
class PentaMiri:
    """五行：64卦归宫五行"""
    def __init__(self):
        self.pentaMiri = None

    def assignYypToPentaMiri(self, yyp):
        if yyp.isCompleted():
            self.pentaMiri = Const.PentaMiriEnum.FIRE
        else:
            self.pentaMiri = None
        print(self.pentaMiri)

class Lemon:
    """柠檬"""
    def __init__(self):
        self.yyp = Yyp()
        self.pentaMiri = PentaMiri()

    def feed(self, food):
        self.yyp.append_xxxv(food)
        self.pentaMiri.assignYypToPentaMiri(self.yyp)

if __name__ == "__main__":
    lemon = Lemon()
    for i in range(13):
        lemon.feed(XxxvObj(Const.XxxvEnum.OLD_BDEM))
