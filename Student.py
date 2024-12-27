students = []

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def add_student(name, age, grade):
    students.append(Student(name, age, grade))
    print(f"Student {name}'s information has been added.")

def view_students():
    if not students:
        print("No students in the system.")
    else:
        print("List of students:")
        for student in students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

def delete_student(name):
    for student in students:
        if student.name == name:
            students.remove(student)
            print(f"Student {name} has been removed.")
            return
    print(f"Student {name} not found.")

# Menu
while True:
    print("\n***** Menu *****")
    n = int(input("Choose a number to \n1 Add a student.\n2 View all students.\n3 Delete a student.\n4 Exit --> "))
    match n:
        case 1:
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            add_student(name, age, grade)
        case 2:
            view_students()
        case 3:
            delete_student(input("Enter the name to delete: "))
        case 4:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
