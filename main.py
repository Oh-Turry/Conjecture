from pythagoras import Pythagorean
from quadratic_formula import Quadratic


def basic():
    # Addition calculation
    if method == "+":
        print("You have selected addition!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        answer = first + second
        print("{} plus {} is equal to {}".format(first, second, answer))

    # Subtraction calculation
    if method == "-":
        print("You have selected subtraction!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        print(
            "Enter a if you want to subtract {first} from {second},\nEnter b if you want to subtract {second} from {first}.".format(
                first=first, second=second
            )
        )
        option = input("Enter here: ")

        # Options to decide which number to subtract from.
        if option == "a":
            answer = second - first
            print("{} minus {} is equal to {}".format(second, first, answer))

        elif option == "b":
            answer = first - second
            print("{} minus {} is equal to {}".format(first, second, answer))

    # Division calculation
    if method == "/":
        print("You have selected division!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        print(
            "Enter a if you want to divide {first} by {second},\nEnter b if you want to divide {second} by {first}.".format(
                first=first, second=second
            )
        )
        option = input("Enter here: ")

        # Options to decide which number to divide from.
        if option == "a":
            answer = first / second
            print("{} / {} is equal to {}".format(second, first, answer))

        elif option == "b":
            answer = second / first
            print("{} / {} is equal to {}".format(first, second, answer))

    # Multiplication calculation
    if method == "*":
        print("You have selected multiplication!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        answer = first * second
        print("{} times {} is equal to {}".format(first, second, answer))

    # Quadratic Calculation
    if method == "q":
        print("You have selected quadratic solver!")
        a = float(input("Please enter the value of a: "))
        b = float(input("Please enter the value of b: "))
        c = float(input("Please enter the value of c: "))
        Quadratic(a, b, c).quadratic()

    # Pythagorean Calculation
    if method == "p":
        Pythagorean.pythagoras()


print(
    "+ for addition\n- for subtraction\n/ for division\n* for multiplication\nq for Quadratic Solver\np for Pythagoras Solver"
)
method = input("Input: ")
basic()
