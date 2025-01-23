i = 0
numbers = []
while (True):
    print(" enter 0 to exit the loop section")
    np_num = int(input("enter the number : "))
    if (np_num != 0):
        numbers.append(np_num)
        i =+ 1
    else :
        break
count = len(numbers)
x = 1
y = 0
while (y == count):
    while(x == count):
        if (numbers[y] == numbers[x]):
            number.remove(numbers[x])
        x += 1
    y += 1
print(numbers)