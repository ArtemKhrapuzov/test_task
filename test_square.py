import unittest

from square import Square


class TestSquare(unittest.TestCase):
    """Тест для класса Square"""

    def test_area_of_a_circle(self):
        area_circle = Square()
        self.assertEqual(area_circle.area_of_a_circle(5), 78.54)
        self.assertEqual(area_circle.area_of_a_circle(0), 0.00)
        self.assertRaises(ValueError, area_circle.area_of_a_circle, -5)

    def test_area_of_a_triangle(self):
        area_triangle = Square()
        self.assertEqual(area_triangle.area_of_a_triangle(4, 4, 5), 'Площадь треугольника равна 8')
        self.assertEqual(area_triangle.area_of_a_triangle(3, 4, 5), 'Площадь прямоугольного треугольника равна 6')
        self.assertEqual(area_triangle.area_of_a_triangle(3, 3, 3), 'Площадь треугольника равна 4')
        self.assertRaises(ValueError, area_triangle.area_of_a_triangle, -5, 10, 7)
        self.assertRaises(ValueError, area_triangle.area_of_a_triangle, -5, -10, -7)
        self.assertRaises(ValueError, area_triangle.area_of_a_triangle, 5, 10, 70)


if __name__ == '__main__':
    unittest.main()
