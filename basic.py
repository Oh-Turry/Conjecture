def basic():
    # Addition calculation
    if method == "+":
        print("You have selected addition!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        answer = first + second
        display = "{} plus {} is equal to {}"
        print(display.format(first, second, answer))

    # Subtraction calculation
    if method == "-":
        print("You have selected subtraction!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        value = "Enter a if you want to subtract {first} from {second},\nEnter b if you want to subtract {second} from {first}."
        print(value.format(first=first, second=second))
        option = input("Enter here: ")

        # Options to decide which number to subtract from.
        if option == "a":
            answer = second - first
            display = "{} minus {} is equal to {}"
            print(display.format(second, first, answer))

        elif option == "b":
            answer = first - second
            display = "{} minus {} is equal to {}"
            print(display.format(first, second, answer))

    # Division calculation
    if method == "/":
        print("You have selected division!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        value = "Enter a if you want to divide {first} by {second},\nEnter b if you want to divide {second} by {first}."
        print(value.format(first=first, second=second))
        option = input("Enter here: ")

        # Options to decide which number to divide from.
        if option == "a":
            answer = first / second
            display = "{} / {} is equal to {}"
            print(display.format(second, first, answer))

        elif option == "b":
            answer = second / first
            display = "{} / {} is equal to {}"
            print(display.format(first, second, answer))

    # Multiplication calculation
    if method == "*":
        print("You have selected multiplication!")
        first = float(input("Please enter the first number: "))
        second = float(input("Please enter the second number: "))
        answer = first * second
        display = "{} times {} is equal to {}"
        print(display.format(first, second, answer))


print("+ for addition\n- for subtraction\n/ for division\n* for multiplication")
method = input("Input: ")
basic()
