password = "python123"
chanses = 3
while (True):
    print(f"you have {chanses} chanses to guess the password")
    guess = input("enter your guess : ")
    if (guess == password ):
        print("wellcome")
        break
    elif(guess != password and chanses == 1):
        print("you are not allow to enter")
        break
    else:
        print ("-------------------------------------------------------------")
        print("please try again")
        chanses = chanses -1