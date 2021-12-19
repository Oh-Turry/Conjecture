import math


class Quadratic:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def quadratic(self):
        # Making things more readable....
        b = float(self.b)
        a = float(self.a)
        c = float(self.c)

        # Calculating the first number using addition.
        powered_b = math.pow(b, 2)
        multiplier = powered_b - 4 * (a * c)
        multiplier = float(multiplier)
        multiplier_2 = 2 * a
        square_root = multiplier ** 2
        first_answer = -b + square_root / multiplier_2
        print(f"The first answer for x is {first_answer}")

        # Calculating the second number using subtraction
        powered_b = math.pow(b, 2)
        multiplier = powered_b - 4 * (a * c)
        multiplier_2 = 2 * a
        square_root = multiplier ** 2
        second_answer = -b - square_root / multiplier_2
        print(f"The second answer for x is {second_answer}")
