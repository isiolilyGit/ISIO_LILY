#Method overriding
class Vehicle:
    def __init__(self, name):
        self.name = name
       
    def display_details(self):
        print(f"The vehicle is {self.name}")

class Car(Vehicle):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model
    
    def display_details(self):
        super().display_details()
        print(f"The {self.name} car is of: {self.model}")

class Truck(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
        
    def display_details(self):
        super().display_details()
        print(f"The {self.name}'s required load capacity is {self.capacity}")

#Asking the user to input the vehicle type
vehicle_type = input("Enter the vehicle type (car/truck)\n").strip().lower()

#Checking the vehicle type
if vehicle_type == "car":
    name = input("What's the car's name: ")
    model = input("What's the car's model: ")

    car = Car(name, model)
    print("\n Car's details")
    car.display_details()
    print(f"\n The car's MRO\n{Car.__mro__}")

elif vehicle_type == "truck":
    name = input("What's the truck's name: ")
    capacity = input("Of what capacity do you require?: ")

    truck = Truck(name, capacity)
    print("\n Truck's details")
    truck.display_details()
    print(f"\n The truck's MRO\n{Car.__mro__}")

else:
    print("Invalid car type")





