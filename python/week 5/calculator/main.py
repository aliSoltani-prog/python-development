import operators

while True:
    print("1.additional")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.radical")
    print("6.Cotangent")
    print("7.Tangent")
    print("8.Sinos")
    print("9.Cosinos")
    print("E.exit")
    menu = print("what do you want to do  : ")
    match menu:
        case "1" :
            try:
                first = int(input("Enter the first number : "))
                second = int(input("Enter the second number : "))
                opratroes.additional(first=first , second=second)
            except :
                print("invalid input")
        case "2" : 
            try:
                first = int(input("Enter the first number : "))
                second = int(input("Enter the second number : "))
                opratroes.Subtraction(first=first , second=second)
            except:
                print("invalid input")
        case "3" : 
            try:
                first = int(input("Enter the first number : "))
                second = int(input("Enter the second number : "))
                opratroes.Multiplication(first=first , second=second)
            except:
                print("invalid input")
        case "4" :
            try:
                first = int(input("Enter the first number : "))
                second = int(input("Enter the second number : "))
                opratroes.Division(first=first , second=second)
            except:
                print("invalid input")
        case "5" :
            try:
                num = int(input("enter the number you want to see it's root"))
                opratroes.radical(num=num)
            except:
                print("invalid input")
        case "6" :
            try:
                num = int(input("enter the number you want to see it's sinos"))
                opratroes.sin(num=num)
            except:
                print("invalid input")
        case "7" :
            try:
                num = int(input("enter the number you want to see it's cosinos"))
                opratroes.cos(num=num)
            except:
                print("invalid input")
        case "8" :
            try:
                num = int(input("enter the number you want to see it's tangent"))
                opratroes.tan(num=num)
            except:
                print("invalid input")
        case "9" :
            try:
                num = int(input("enter the number you want to see it's ctangent"))
                opratroes.cot(num=num)
            except:
                print("invalid input")
        case "E" :
            break
        case _:
            print("wrong answer. try again.")