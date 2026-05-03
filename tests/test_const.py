import unittest
from penta_lemon.const import Const

class TestConst(unittest.TestCase):

    def setUp(self):
        pass

    def test_const(self):
        self.assertEqual(len(Const.YypCode), 64+8)
        self.assertEqual(Const.YypCode.水火既濟.value, Const.YypCode.火.value + Const.YypCode.水.value)

if __name__ == "__main__":
    unittest.main()