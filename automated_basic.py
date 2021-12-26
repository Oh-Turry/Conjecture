class AutoBasic:
    def __init__(self, first_number, second_number):
        self.first_number = float(first_number)
        self.second_number = float(second_number)

    def division(self):
        print("{} / {} has been initialized".format(self.first_number, self.second_number))
        return self.first_number / self.second_number

    def multiplication(self):
        print("{} * {} has been initialized".format(self.first_number, self.second_number))
        return self.first_number * self.second_number

    def addition(self):
        print("{} + {} has been initialized".format(self.first_number, self.second_number))
        return self.first_number + self.second_number

    def subtraction(self):
        print("{} - {} has been initialized".format(self.first_number, self.second_number))
        return self.first_number - self.second_number
