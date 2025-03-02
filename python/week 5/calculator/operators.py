import math

def additional(first , second):
    print(f"{first} + {second} = {first+second}")

def Subtraction(first , second):
    print(f"{first} - {second} = {first-second}")

def Multiplication(first , second):
    print(f"{first} * {second} = {first*second}")

def Division(first,second):
    print(f"{first} / {second} = {first/second}")

def radical(num):
    print(f"the root of the {num} is {num**0/5}")

def sin(num):
    print(f"the sinos of the {num} is {math.sin(math.radians(num))}")

def cos(num):
    print(f"the cosinos of the {num} is {math.cos(math.radians(num))}")

def tan(num):
    print(f"the Tangent of the {num} is {math.tan(math.radians(num))}")

def cot(num):
    print(f"the Cotangent of the {num} is {1/math.tan(math.radians(num))}")