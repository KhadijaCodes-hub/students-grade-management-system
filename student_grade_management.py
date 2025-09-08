students={}
print("-----Welcome to Students Grade Management System-----")
total_student = int(input("Enter Total No. of students : "))
for i in range(1 , total_student+1):
    student = input(f"Enter Student {i} : ")
    marks = float(input(f"Enter marks of student {i} : "))
    print(f"{student} with marks {marks} has been added.")
    students.update({student:marks})

while True:
    operation = int(input("1 for add\n2 for update\n3 for delete\n4 for view\n5 for exit/stop\n"))
# For adding a new student
    if operation==1:
        add_student = input("Enter new student : ")
        add_marks = float(input("Enter marks : "))
        students.update({add_student:add_marks})
        print(f"New Student {add_student} has been added.")
# For updating an existing student
    elif operation==2:
        updated_stu=input("Enter Student name you want to update : ")
        if updated_stu in students:
            up_marks = float(input("Enter student marks : "))
            students[updated_stu]=up_marks
            print(f"Updated Student {updated_stu}")
# For deleting a student
    elif operation==3:
        del_stu = input("Enter student name you want to delete : ")
        if del_stu in students:
            del students[del_stu]   
            print(f"Student {del_stu} has been deleted successfully")
# For showing all students
    elif operation==4:
        print(f"All Students are : {students}")                         
# To exit the program        
    elif operation==5:
        print("Closing the program...") 
        break
    else:
        print("Invalid Input.")       
