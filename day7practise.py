shop_items = []
cart = []
running = True
# Creating the shop list with user input
num_items = int(input("How many items do you want to add to the shop? "))
for i in range(num_items):
    item = input(f"Enter item {i+1}: ")
    shop_items.append(item)
    print("\nWelcome to the Shop!")
    print("Available items:", shop_items)
while running:
    print("\nOptions: add, remove, view, checkout, exit")
    action = input("What would you like to do? ").lower()
    if action == "add":
        item = input("Enter the item to add: ")
        if item in shop_items:
            cart.append(item)
            print(item, "added to cart.")
        else:
                print("Item not available in the shop.")
    elif action == "remove":
        item = input("Enter the item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
                print("Item not in cart.")
    elif action == "view":
        print("Your cart:", cart)

    elif action == "checkout":
        print("Checking out...")
        print("Items purchased:", cart)
        cart.clear()
        print("Thank you for shopping!")
    elif action == "exit":
            print("Exiting the shop.")
            running = False
    else:
        print("Invalid option.")
