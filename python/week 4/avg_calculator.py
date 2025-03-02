marks = 0
i = 1
while (True):
    print(" enter 0 to exit the loop section")
    np_num = float(input("enter the mark : "))
    if (np_num != 0 and np_num<=20 ):
        marks += np_num
        i += 1
    elif (np_num>20):
        print('''tyr again
        the mark shoulde be between 0 and 20''')
    else :
        break
#print(marks)
print(f"the avrage is {(round(marks/i))}")