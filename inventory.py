#Displaying and updating items inventory items

items = {}

#A function to add items to the dictionary
def add_item(name, quantity, price):
    if name not in items:
        items[name] = {"quantity":quantity, "price":price}
        print(f"The item {name} has been added to the list")
    
    else:
        items[name]["quantity"] += quantity
        items[name]["price"] = price

#A function to update items and their details
def update_item():
    name = input("Enter the item's name to be updated ")
    if name in items:
        new_quantity = int(input(f"Enter the new quantity for {name} "))
        new_price = float(input(f"Enter the new price {name} "))
        if new_quantity:
            items[name]["quantity"] = int(new_quantity)
        if new_price:
            items[name]["price"] = float(new_price)

        print("The updated list\n")
        for name, details in items.items():
            print(f"{details['quantity']} {name}s cost {details['price']:.2f}")
             
    else:
        print(f"Item {name} not found")

#A function to display the items
def display_items():
    if not items:
        print("There are no items to display")
    
    else:
        for name, details in items.items():
            print(f"{details['quantity']} {name}s cost {details['price']:.2f}")
        

def main():
    #Prompting the user to make a choice
    #to add or remove or display or update items
    while True:
        print("Inventory menu")
        print("1. Add items to the list")
        print("2. Remove items from the list")
        print("3. Update items of the list")
        print("4. Display items of the list")
        print("5. Exit")

        choice = input("Enter a choice from the menu\n")

        if choice == "1":
            name = input("Enter the item's name ")
            quantity = int(input("How many of the items do you want "))
            price = float(input("Enter the price "))
            add_item(name, quantity, price)
        
        elif choice == "3":
            update_item()

        elif choice == "4":
            display_items()
        
        elif choice == "5":
            break

        else:
            print("Invalid choice")


main()