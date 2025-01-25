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
    print (f"this is your list {numbers}")
print (f"this is your list {numbers}")
i = 0
fit_numbers = []
for x in range (len(numbers)):
    exist = numbers[x] in fit_numbers
    if (exist == False):
        fit_numbers.append(numbers[x])
        i += 1
print(f"and this is fited numbers : {fit_numbers}")