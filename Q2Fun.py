#2. Write Functions:
# add_student: Adds a new student to the list.
# view_students: Displays all students in the system.
# delete_student: Removes a student based on their name.
students = ["sosina" , "Ayele" , "kebede" ," Temesgen" , "Alice"]

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

view_students()
# Adding a new student
add_student("Abebe")

# Viewing all students
view_students()

# Deleting a student
delete_student("Alice")

# Viewing all students again
view_students()
