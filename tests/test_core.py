import unittest
from src.penta_lemon.core import Lemon, Const, XxxvObj

class TestCore(unittest.TestCase):

    def setUp(self):
        self.lemon = Lemon()

    def test_lemon(self):
        for i in range(13):
            self.lemon.feed(XxxvObj(Const.XxxvEnum.OLD_BDEM))

if __name__ == "__main__":
    unittest.main()