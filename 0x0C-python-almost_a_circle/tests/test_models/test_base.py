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

    def test_H_to_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}]')

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    ef test_H_test_from_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        s = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"foobarrooo": 989898}]
        s = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        s = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

    def test_J_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_K_load_from_file(self):
        '''Tests load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == '__main__':
    unittest.main()
