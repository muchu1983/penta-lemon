import unittest
from src.penta_lemon.main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        with self.assertRaises(SystemExit) as ctx:
            main()
        self.assertEqual(ctx.exception.code, 0)

if __name__ == "__main__":
    unittest.main()