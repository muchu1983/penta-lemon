from penta_lemon.const import Const
"""核心类"""
class Xxxv:
    """爻：万物分阴阳"""
    def __init__(self, xxxv_code:Const.XxxvCode):
        self.xxxvCode = xxxv_code

    def getXxxvCode(self):
        return self.xxxvCode

class OctaNopoPentaMiri:
    """八宫五行：64卦归八宫五行"""
    def __init__(self):
        self.pentaMiriCode = None
        self.octaNopoCode = None
        self.yyp = None

    def getPentaMiriCode(self):
        return self.pentaMiriCode

    def getOctaNopoCode(self):
        return self.pentaMiriCode

    #64卦归八宫五行
    def assignYypToPentaMiri(self, yyp):
        if yyp.isCompleted():
            self.yyp = yyp
            pass #查出该卦的所属八宫及八宫对应的五行
            self.octaNopoCode = Const.OctaNopoCode.HEAVEN
            self.pentaMiriCode = Const.PentaMiriCode.FIRE

    #8宫五行卦转爻(进位) 6进制但每一位有64值域
    def completedYypToXvvv(self) -> Xxxv|None:
        if self.yyp.isCompleted():
            pass
            return Xxxv(Const.XxxvCode.YOUNG_BDEM)
        else:
            return None

    #清除状态
    def clear(self):
        self.yyp = None
        self.octaNopoCode = None
        self.pentaMiriCode = None

class Yyp:
    """卦：六爻成卦"""
    def __init__(self):
        self.sixXxxv = [] #六爻
        self.onpm = OctaNopoPentaMiri()

    def getSixXxxvList(self):
        return self.sixXxxv

    def append_xxxv(self, xxxv):
        if len(self.sixXxxv) >= 6:
            self.sixXxxv.clear() #清空重来
        self.sixXxxv.append(xxxv)
    
    def isCompleted(self):
        return True if len(self.sixXxxv) == 6 else False

    def completedYypToOnpm(self) -> OctaNopoPentaMiri|None:
        if self.isCompleted():
            self.onpm.assignYypToPentaMiri(self)
            return self.onpm
        else:
            self.onpm.clear()
            return None
        
class Lemon:
    """柠檬"""
    def __init__(self):
        self.yyp = Yyp()
        self.octaNopoPentaMiri = None

    def feedXxxv(self, xxxv):
        self.yyp.append_xxxv(xxxv)
        self.octaNopoPentaMiri = self.yyp.completedYypToOnpm()
        if self.octaNopoPentaMiri is not None:
            self.octaNopoPentaMiri.completedYypToXvvv()

    def getOctaNopoPentaMiri(self):
        return self.octaNopoPentaMiri

    def getYyp(self):
        return self.yyp
