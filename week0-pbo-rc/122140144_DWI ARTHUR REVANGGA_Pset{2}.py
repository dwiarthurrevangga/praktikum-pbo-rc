num_students = int(input("Enter the number of students : "))

students_data = {}

for students in range (num_students) :
  name= input("Enter student's name : ")
  grade = int(input("Enter student's grade : ))
  students_data[name] = grade
  print("Student's data successfully added\n")

print("Student's Data : \n")

for name, grade in students_data.items() :
  print(f"{name} : {grade}")
