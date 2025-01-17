print ('''enter the the color to do blow acts :
red : stop
yellow : slow down
green : go''')
flag = True
while (flag == True):
    print ("enter the E to exit the program")
    color = input("enter the color you want: ")
    print ("-------------------------------------------------------------")
    if (color[0] == "r"):
        print ("stop")
    elif(color[0] == "y"):
        print ("slow down")
    elif(color[0] == "g"):
        print("go")
    elif(color == "E"):
        flag = False
    else:
        print("invalid value")
