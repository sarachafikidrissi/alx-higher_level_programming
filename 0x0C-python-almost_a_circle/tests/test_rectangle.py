import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        # Test the constructor of the Rectangle class
        r1 = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(7, 4)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)  # Default value
        self.assertEqual(r2.y, 0)  # Default value
        self.assertIsNotNone(r2.id)  # Ensure id is not None

        # Check that the IDs are unique
        self.assertNotEqual(r1.id, r2.id)

    def test_access_id(self):
        # Test that you can access the 'id' attribute of a Rectangle instance
        r = Rectangle(8, 6)
        self.assertIsNotNone(r.id)  # Ensure id is not None
        self.assertIsInstance(r.id, int)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
            Rectangle(10, {})
            Rectangle(1, 2, "sara", [])
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectangle(10, 0)
            Rectangle(10, 12, -1, 5)
            Rectangle(10, 12, 3, -6)

    def test_display(self):
        r1 = Rectangle(2, 2)
        r2 = Rectangle(2, 3, 2, 2)
        import io
        from unittest.mock import patch

        with patch('sys.stdout', new_callable=io.StringIO) as r1_stdout:
            r1.display()
            r1_output = r1_stdout.getvalue()

            r1expected_output = "##\n##\n"
        self.assertEqual(r1_output, r1expected_output)
        with patch('sys.stdout', new_callable=io.StringIO) as r2_stdout:
            r2.display()
            printed_output = r2_stdout.getvalue()

            expected_output = "\n\n  ##\n  ##\n  ##\n"

        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)

        import io
        from unittest.mock import patch
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(r1)
            printed_output = mock_stdout.getvalue()

            expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(printed_output, expected_output)


if __name__ == '__main__':
    unittest.main()
