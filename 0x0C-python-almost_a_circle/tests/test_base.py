import unittest
from models.base import Base



class TestBase(unittest.TestCase):

    def test_id(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(4)
        self.b4 = Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 4)
        self.assertEqual(self.b4.id, 3)


if __name__ == '__main__':
    unittest.main()
