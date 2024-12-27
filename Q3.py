"""Implement a Menu:
Options
Add a student.
View all students.
Delete a student.
Exit the program."""
students = []

def add_student(name):
    students.append(name)
    print(f"Student {name} has been added.")
def view_students():
    if not students:
        print("No students in the system.")
    else:
        print("List of students:")
        print(students)
def delete_student(name):
    students.remove(name)
    print(f"Student {name} has been removed.")
print()
while True:
    print ("*****Menu*****")
    n = int(input("choose a number To \n1 Add a student.\n2 View all students.\n3 Delete a student.\n4 Exit --> "))
    match n:
        case 1:
            add_student(input("Enter the name : "))
        case 2:
            view_students()
        case 3:
            delete_student(input("Enter the name to delete : "))
        case 4:
            print("Good Bye")
            break
