numbers = []
i = 0
picker = 0
while (True):
    print(" enter 0 to exit the loop section")
    np_num = int(input("enter the number : "))
    if (np_num != 0):
        numbers.append(np_num)
        i =+ 1
    else :
        break
i = 0
print("-----------------------------------------------")
print(numbers)
turn_count = int(input("enter the count of turning : "))
while (turn_count != 0):
    picker = numbers[0]
    numbers.remove(numbers[0])
    numbers.append(picker)
    turn_count -= 1 
print(f"the final result is {numbers}")