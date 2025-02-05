count = int(input("enter the count of students : "))
students_name = []
students_grade = []
students_age = []

np_stu = {}
for x in range (count) :
    np_stu["name"]= input("enter the name : ")
    students_name.append(np_stu["name"])
    np_stu["age"] = int(input("enter the age : "))
    students_age.append(np_stu["age"])
    np_stu["grade"] = float(input("enter the grade : "))
    students_grade.append(np_stu["grade"])
    print(f"{np_stu["name"]} has {np_stu["age"]} years old and he get {np_stu["grade"]} at school")
    print("----------------------------------------------------------")
    #print(students_name)
    #print(students_age)
    #print(students_grade)
search = input("which student do you looking for ? ")
flag = search in students_name 
if flag == True:
    print("----------------------------------------------------------")
    search = students_name.index(search)
    print(f"{students_name[search]} has {students_age[search]} years old and he get {students_grade[search]} at school")
else:
    print("----------------------------------------------------------")
    print("student you looking does not study here")


