i = 0
grades = []
while (True):
    print(" enter 0 to exit the loop section")
    np_num = int(input("enter the grade : "))
    if (np_num != 0):
        grades.append(np_num)
        i =+ 1
    else :
        break
i = 0
sum_num = 0
for x in range (len(grades)):
    sum_num += grades[x]
    i += 1
avrage = sum_num/i
print(f"your grade is {avrage}")