shop_items=[]
cart=[]
running = True

No_items=int(input("Enter the number of items:"))

for i in range(No_items):
    clothe=input(f"Enter the clothe{i+1} name:")
    shop_items.append(clothe)
print("---welcome to our shop!!!---")
print(shop_items)

while running:
    print("\n options : add,remove,view,checkout,exit")
    action=input("Enter your option:").lower()

    if action == "add":
        item=input("Enter you item to add:")
        if item in shop_items:
            cart.append(item)
            print("your item is added")
        else:
            print("your item is not available")
    elif action == "remove":
        item=input("Enter you item to remove:")
        if item in cart:
            cart.remove(item)
            print("your item is removed")
        else:
            print("item is not in cart")
    elif action == "view":
        print("your cart!!", cart)

    elif action == "checkout":
        print("checking out")
        print("item you have purchased:",cart)
        cart.clear()
        print("Thankyou for ur purchase , visit our shop once!!")
    elif action == "exit":
        print("Existing the shop!!")
        running = False
    else:
    print("Invalid option")
