'STUDENT INFORMATION SYSTEM USING TUPLE'

name=input("Enter your name :")
age=int(input("Enter your age:"))
department=input("Enter your department:")
grade=input("Enter your grade:")


'creating a tuple'

student=(name,age,department,grade)
print("student detail:",student)

'positive and negative indexing '

print("name of the student:",student[0])
print("grade of the student:",student[-1])


'slicing'

print("Name and Age of the student:",student[0:2])



'Iterating'

print("Iteration over tuple")
for info in student:
    print("-",info)


'length of the tuple'
print("Length of the student tuple:",len(student))

print("\n Q8: How many times does the department appear?\nA:",
student.count(department))

'indexing of an element'
print("index of the department:",student.index(department))



"to add the hostel and sports "

extra=("Hostel","Sports")

modify=student+extra

print("modified student list:",modify)


"converting the tuple into list for update and again into tuple"

student_list=list(student)
print("List of the student:",student_list)

student_list[1]=student_list[1] + 1
print("updating the age in list :",student_list[1])

student=tuple(student_list)

print("converted into tuple after the updation :",student)

