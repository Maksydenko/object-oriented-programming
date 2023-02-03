# Task 1
class Rational:
    def __init__(self, numberator=4, denominator=10):
        numberator, denominator = self.reduce_fraction(numberator, denominator)
        self.numberator = numberator
        self.denominator = denominator

    @staticmethod
    def reduce_fraction(numberator, denomunator):
        from math import gcd

        gcd = gcd(numberator, denomunator)
        numberator //= gcd
        denomunator //= gcd
        return numberator, denomunator

    def get_float(self):
        return self.numberator / self.denominator

    def __str__(self):
        return f"{self.numberator}/{self.denominator}; "\
            f"float {self.get_float()}"


# Task 2
class Rectangle:
    def __init__(self, width=80, height=60):
        if width <= 0 or height <= 0:
            raise ValueError("Side cannot be equal to or less than 0")
        self.width = Rectangle.limit_side(width)
        self.height = Rectangle.limit_side(height)

    MAX_SIZE = 100

    @classmethod
    def limit_side(cls, side):
        if side > cls.MAX_SIZE:
            return cls.MAX_SIZE
        return side

    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return f"{perimeter} cm"

    def get_square(self):
        square = self.width * self.height
        return f"{square} cm²"

    def __str__(self):
        return f"Perimeter: {self.get_perimeter()};" \
            f"square: {self.get_square()}"
