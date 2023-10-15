#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is test_square module
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_integers(self):
        s1 = Square(5)
        s2 = Square(5, 3)
        s3 = Square(5, 3, 2)
        s4 = Square(5, 3, 2, 12)

        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s3.y, 2)
        self.assertEqual(s4.id, 12)

    def test_raises(self):
        with self.assertRaises(TypeError):
            Square("5")
            Square(5, {})
            Square(5, 's', [1, 2, 3])
            Square(1, 2, 3, 'id')
        with self.assertRaises(ValueError):
            Square(0)
            Square(-1, 0)
            Square(5, -5)
            Square(5, 2, -5)

    def test_area(self):
        s = Square(3, 3)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        s2 = Square(2, 2)

        import io
        from unittest.mock import patch

        with patch('sys.stdout', new_callable=io.StringIO) as s2_stdout:
            s2.display()
            s2_output = s2_stdout.getvalue()

            s2expected_output = "  ##\n  ##\n"
        self.assertEqual(s2_output, s2expected_output)

    def test_str(self):
        """
        Test for __str__ method
        """
        S = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(S))

    def test_args_kwargs(self):
        """
        Test for update method: kwargs
        """
        S = Square(1, 2, 3, 4)
        S.update(6, id=7)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 1, 2, 3])
        S.update(6, 7, x=9, y=10)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(width=7, id=6, height=8)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(x=40, y=5)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 40, 5])

    def test_dictionary(self):
        """
        Tests for dictionary method
        """
        S = Square(100, 300, 400, 500)
        S_dict = S.to_dictionary()
        self.assertEqual(S_dict['size'], 100)
        self.assertEqual(S_dict['x'], 300)
        self.assertEqual(S_dict['y'], 400)
        self.assertEqual(S_dict['id'], 500)


if __name__ == '__main__':
    unittest.main()
