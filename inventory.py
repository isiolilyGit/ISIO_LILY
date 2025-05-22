#Displaying and updating items inventory items

items = {}

def add_item(name, quantity, price):
    if name not in items:
        items[name] = {"quantity":quantity, "price":price}
        print(f"The item {name} has been added to the list")
    
    else:
        items[name]["quantity"] += quantity
        items[name]["price"] = price