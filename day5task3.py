phone password verification


ph_code="123"

for i in range(5):
    
    user_code=input("Enter your password pin:")
    if ph_code==user_code:
        print("you have entered the correct pin!")
        break
    else:
        print("Enter the correct pin")

