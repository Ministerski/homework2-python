import math

# Базовый класс
class Shape:
    def area(self) -> float:
        """Метод для вычисления площади (будет переопределен в наследниках)"""
        pass

    def perimeter(self) -> float:
        """Метод для вычисления периметра (будет переопределен в наследниках)"""
        pass

    def compare_area(self, other_shape: 'Shape') -> str:
        """Сравнение площади текущей фигуры с другой"""
        if self.area() > other_shape.area():
            return "Площадь больше"
        elif self.area() < other_shape.area():
            return "Площадь меньше"
        return "Площади равны"

    def compare_perimeter(self, other_shape: 'Shape') -> str:
        """Сравнение периметра текущей фигуры с другой"""
        if self.perimeter() > other_shape.perimeter():
            return "Периметр больше"
        elif self.perimeter() < other_shape.perimeter():
            return "Периметр меньше"
        return "Периметры равны"

# Класс Квадрат
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return self.side * 4

# Класс Прямоугольник
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2

# Класс Круг
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

# Класс Треугольник (по трем сторонам)
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        # Используем формулу Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# --- Проверка работы кода ---
if __name__ == "__main__":
    sq = Square(5)        # Площадь 25, периметр 20
    rect = Rectangle(4, 6) # Площадь 24, периметр 20
    circ = Circle(3)      # Площадь ~28.27, периметр ~18.84

    print(f"Площадь квадрата: {sq.area()}")
    print(f"Площадь круга: {circ.area():.2f}")
    
    print("--- Сравнения ---")
    print(f"Квадрат vs Прямоугольник (Площадь): {sq.compare_area(rect)}")
    print(f"Квадрат vs Прямоугольник (Периметр): {sq.compare_perimeter(rect)}")
    print(f"Круг vs Квадрат (Площадь): {circ.compare_area(sq)}")