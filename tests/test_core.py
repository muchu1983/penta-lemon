import unittest
from src.penta_lemon.core import Lemon, Const, Xxxv

class TestCore(unittest.TestCase):

    def setUp(self):
        self.lemon = Lemon()

    def test_lemon(self):
        for i in range(5): #前五爻
            self.lemon.feed(Xxxv(Const.XxxvCode.OLD_BDEM))
            self.assertIsNone(self.lemon.getPentaMiri().getPentaMiriCode())
        self.lemon.feed(Xxxv(Const.XxxvCode.OLD_BDEM)) #第六爻
        self.assertIsNotNone(self.lemon.getPentaMiri().getPentaMiriCode())
        self.lemon.feed(Xxxv(Const.XxxvCode.OLD_BDEM)) #第七爻(重置)
        self.assertIsNone(self.lemon.getPentaMiri().getPentaMiriCode())

if __name__ == "__main__":
    unittest.main()