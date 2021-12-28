import math


class Pythagorean:
    def pythagoras():
        print("You have selected the 'Pythagoras Solver'!")
        form = int(input("1 = height, 2 = base and 3 = hypotenuse\nPlease enter what you want to find: "))

        # Calculation Proccess
        values = {1: "height", 2: "base", 3: "hypotenuse"}
        val = values.get(form)
        initialize = "Finding the {}...".format(val)
        print(initialize)
        if form == 1:
            b = float(input("Please enter the value of b: "))
            c = float(input("Please enter the value of c: "))
            base = math.pow(b, 2)
            hypotenuse = math.pow(c, 2)
            answer = math.sqrt(hypotenuse - base)
            print(round(answer, 2))
        elif form == 2:
            a = float(input("Please enter the value of a: "))
            c = float(input("Please enter the value of c: "))
            height = math.pow(a, 2)
            hypotenuse = math.pow(c, 2)
            answer = math.sqrt(hypotenuse - height)
            print(round(answer, 2))
        elif form == 3:
            a = float(input("Please enter the value of a: "))
            b = float(input("Please enter the value of b: "))
            height = math.pow(a, 2)
            base = math.pow(b, 2)
            answer = math.sqrt(height + base)
            print(round(answer, 2))
        else:
            raise
