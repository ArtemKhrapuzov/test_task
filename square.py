import math


class Square:
    """Расчет площади фигур"""

    def area_of_a_circle(self, radius):
        """Расчет площади круга"""
        if radius < 0:
            raise ValueError('Значение должно быть положительным.')
        return round(math.pi * radius ** 2, 2)

    def area_of_a_triangle(self, a, b, c):
        """Расчет площади треугольника"""
        if a < 0 or b < 0 or c < 0:
            raise ValueError('Значение должно быть положительным.')
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            lst = [a, b, c]
            max_num = max(lst)
            lst.remove(max_num)
            if max_num**2 == lst[0]**2 + lst[1]**2:
                return f'Площадь прямоугольного треугольника равна {round((p * (p - a) * (p - b) * (p - c)) ** 0.5)}'
            else:
                return f'Площадь треугольника равна {round((p * (p - a) * (p - b) * (p - c)) ** 0.5)}'

        else:
            raise ValueError('Треугольник с заданным сторонами не существует')



sq = Square()
print(sq.area_of_a_triangle(3,3,3))






