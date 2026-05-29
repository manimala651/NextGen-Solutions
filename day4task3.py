print("--based on the age category , to print the entry fees-- ")


age=int(input("Enter your age : "))

if 0<=age<=5:
    print("you are baby!!,so no need to pay entry fees ")
elif 6<=age<=12:
    print("you are child !!,so your entry fees is 20")
elif 13<=age<=19:
    print("you are teenage!!,so your entry fees is 50")
elif 20<=age<=60:
    print("you are adult!!,so your entry fees is 100")
elif 60<=age<=100:
    print("you are senior citizen!!,your entry fees is 60")
else:
    print("Invalid age!!")
