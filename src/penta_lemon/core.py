from enum import Enum
"""核心类"""
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

class Xxxv:
    """爻：万物分阴阳"""
    def __init__(self, xxxv_code:Const.XxxvCode):
        self.xxxvCode = xxxv_code

class OctaNopoPentaMiri:
    """八宫五行：64卦归八宫五行"""
    def __init__(self):
        self.pentaMiriCode = None
        self.yyp = None

    def getPentaMiriCode(self):
        return self.pentaMiriCode

    def assignYypToPentaMiri(self, yyp):
        if yyp.isCompleted():
            self.yyp = yyp
            self.pentaMiriCode = Const.PentaMiriCode.FIRE

    def completedYypToXvvv(self, yyp) -> Xxxv|None:
        if yyp.isCompleted():
            #8宫五行卦转爻(进位)
            #6进制但每一位有64值域
            pass
            return None
        else:
            return None

class Yyp:
    """卦：六爻成卦"""
    def __init__(self):
        self.sixXxxv = [] #六爻

    def append_xxxv(self, xxxv):
        if len(self.sixXxxv) >= 6:
            self.sixXxxv.clear() #清空重来
        self.sixXxxv.append(xxxv)
    
    def isCompleted(self):
        return True if len(self.sixXxxv) == 6 else False

    def completedYypToOnpm(self) -> OctaNopoPentaMiri|None:
        if self.isCompleted():
            #64卦归八宫五行
            onpm = OctaNopoPentaMiri()
            onpm.assignYypToPentaMiri(self)
            return onpm
        else:
            return None
        
class Lemon:
    """柠檬"""
    def __init__(self):
        self.yyp = Yyp()
        self.octaNopoPentaMiri = None

    def feed(self, food):
        self.yyp.append_xxxv(food)
        self.octaNopoPentaMiri = self.yyp.completedYypToOnpm()
        if self.octaNopoPentaMiri is not None:
            self.octaNopoPentaMiri.completedYypToXvvv(self.yyp)

    def getOctaNopoPentaMiri(self):
        return self.octaNopoPentaMiri
