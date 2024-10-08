import math


class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = False


    def get_color(self):
        """Возвращает список RGB цветов"""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """ служебный, принимает параметры r, g, b, который проверяет корректность
         переданных значений перед установкой нового цвета. Корректным цвет:
         все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)"""
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        """принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
         предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним"""
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("Некорректные значения цвета. Цвет не изменен.")

    def __is_valid_sides(self, *sides):
        """принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
         и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях."""
        for side in sides:
            if len(sides) == self.sides_count or len(sides) == 1 and isinstance(side, int) and side > 0:
                return True
            else:
                return False

    def get_sides(self):
        """должен возвращать значение я атрибута __sides."""
        return list(self.__sides)

    def __len__(self):
        """ должен возвращать периметр фигуры."""
        sides = self.get_sides()
        if len(sides) == 12:
            if type(self.get_sides()) == list:
                return sum(self.get_sides())
            else:
                per = [side[0] for side in self.__sides]
                return  sum(per)
        return sum(sides)

    def set_sides(self, *new_sides):
        """ должен принимать новые стороны, если их количество не равно sides_count,
         то не изменять, в противном случае - менять."""
        if self.__is_valid_sides(*new_sides) and self.sides_count == 12: # для куба
            self.__sides =  new_sides * self.sides_count
        elif self.__is_valid_sides(*new_sides): #для остальных
            self.__sides = new_sides
        else:
            print("Некорректные значения сторон. Стороны не изменены.")
            self.__sides = [1] * self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)
        self.set_sides(circumference)  # Устанавливаем длину окружности как сторону
        self.__radius = circumference / (2 * math.pi)  # Рассчитываем радиус

    def get_square(self):
        """Возвращает площадь круга."""
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.set_sides(a, b, c)  # Устанавливаем стороны треугольника

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона."""
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))



class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color,sides)


    def get_volume(self):
        """возвращает объём куба."""
        edge_length = self.get_sides()[0]# Длина ребра
        if edge_length == 1:
            return 12
        return edge_length ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # Цвет и длина окружности
    cube1 = Cube((222, 35, 130), 6)
    triangel1 = Triangle ( (222, 35, 130), 12, 11,13)


    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print('Вывод: (55, 66, 77) -',circle1.get_color())  # Вывод: (55, 66, 77)

    cube1.set_color(300, 70, 15)  # Не изменится
    print('Вывод: (222, 35, 130)- ',cube1.get_color())  # Вывод: (222, 35, 130)

    # Проверка на изменение сторон:
    triangel1.set_sides(2, 3, 4 )
    print('Вывод 2, 3, 4 -', triangel1.get_sides())
    print("Вывод сторон до изменения", cube1.get_sides())
    cube1.set_sides(5, 3, 12, 4 )  # Не изменится
    print('Вывод: [1] * 12 -',cube1.get_sides())  # Вывод: [1] * 12
    cube1.set_sides(5)  # изменится
    print('Вывод: [5] * 12 -', cube1.get_sides())  # Вывод: [5] * 12

    #
    circle1.set_sides(15)  # Изменится
    print('Вывод 15 -',circle1.get_sides())  # Вывод: [15]
    #
    # Проверка периметра (круга), это и есть длина:
    print('Периметр круга -',len(circle1))  # Вывод: Периметр круга (длина окружности)

    # Проверка объёма (куба):
    print('Объем куба -', cube1.get_volume())  # Вывод: Объем  куба

    #дополнительные проверки
    print('Периметр куба -', cube1.__len__())
    print('Периметр треугольника -', triangel1.__len__())
    print('стороны треугольника - ',triangel1.get_sides())
    print('Площадь круга - ', circle1.get_square())
    print('Радиус круга - ', circle1.get_radius())