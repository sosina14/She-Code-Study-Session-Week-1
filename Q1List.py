#1. a List of Students:
# Create a list of dictionaries, each representing a student
# with attributes like name, age, and grade.
student = [
  {"name": "Sosina", "age": 22, "grade": "A"},
  {"name" : "Kebede", "age": 20, "grade": "A"},
  {"name": "Abebe", "age": 23, "grade": "B"},
  {"name": "rediet", "age": 21, "grade": "C"},
  {"name": "Charlie", "age": 19, "grade": "A"},
]
#print(student)
for students in student:
    print(f"Name: {students['name']}, Age: {students['age']}, Grade: {students['grade']}")