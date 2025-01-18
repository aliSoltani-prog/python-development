flag = True
print("this program will atke your grade and show the situation you in it")
while(flag==True):
    print ("enter the 0 to exit the program")
    grade = int(input("enter the grade you get (between 0 and 100): "))
    print ("----------------------------------------------------------------------")
    if (grade>100 and grade<0):
        print("please try again")
    elif(grade>90 and grade<= 100):
        print("Exellent")
    elif(grade<=90 and grade>70):
        print("good")
    elif(grade<=70 and grade>=50):
        print("need more effort")
    elif(grade == 0):
        flag = False
    else:
        print("you failed")