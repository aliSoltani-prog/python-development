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
i = 0 
while i < len(numbers):
    if (numbers[i] % 2 != 0):
        numbers.pop(i)
    else :
        i += 1

print(numbers)
