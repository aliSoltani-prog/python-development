print ("i can help you to decide that you want to go to cinema or not")
print ("-------------------------------------------------------------")
firstQ = input("is your favorite film plaing ? ")
secondQ = input("is the cinema ticket cheap ? ")
thirdQ = input("do you have free time ? ")
print ("-------------------------------------------------------------")
if (firstQ[0] and secondQ[0] and thirdQ[0] == "y" ):
    print("you are allow to go to cinema")
else:
    print("you are not allow to go to cinema")
