import unittest

from src.Open_Close.Logical_Operators import LogicalOp


class ImageIOTest(unittest.TestCase):

    def SetUP(self):
        self.logOP = LogicalOp()

    def test_LogicalAND(self):
        self.assertEqual(True, self.logOP.logicalAND([True]))

    def test_LogicalOR(self):
        self.assertEqual(True, self.logOP.logicalOR([True, False]))

    def test_LogicalMAJ(self):
        self.assertEqual(True, self.logOP.logicalMAJ([True, True, False]))


    if __name__ == '__main__':
        unittest.main()