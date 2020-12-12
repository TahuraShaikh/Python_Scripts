# class calculator capable of finding square , cube, squareroot:
class Calculator:
    def __init__(self,num):
        self.num=num

    def Square(self):        # function calculates square of a number
        print(f"Square of {self.num} is {self.num **2}")

    def cube(self):            # function calculates cube of a number
        print(f"Cube of {self.num} is {self.num **3}")

    def squareroot(self):        ## function calculates square-root of a number
        print(f"Square-root of {self.num} is {self.num **0.5}")

n1=Calculator(2)
n1.Square()
n1.cube()
n1.squareroot()