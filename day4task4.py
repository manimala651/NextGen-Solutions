print("--checking if a person is eligible for a loan or not--")

age=int(input("Enter your age:"))
salary=int(input("Enter your salary:"))

if 21<=age<=60:
    print("you are eligible for applying loan!!")
    if salary >=30000:
        print("you can apply for loan")
    else:
        print("you can not able to apply for loan")
else:
    print("you are not eligible for applying loan!!")
