class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def patients_details(self):
        print(f"The patient is called {self.name}")
        print(f"{self.name} is {self.age} years old")

class InPatient(Patient):
    def __init__(self, name, age, room_number):
        super().__init__(name, age)
        self.room_number = room_number

    def patients_details(self):
        print(f"A {self.name} is in room {self.room_number}")

class OutPatient(Patient):
    def __init__(self, name, age, appointment_date):
        super().__init__(name, age)
        self.appointment_date = appointment_date

    def patients_details(self):
        print(f"{self.name}'s appointment is on {self.appointment_date}")

#Asking the user to input the vehicle type
patient_type = input("Are you an (InPatient/OutPatient)\n").strip().lower()

#Checking the vehicle type
if patient_type == "InPatient":
    name = input("What's your name?: ")
    room_number = input("In which room are you?: ")

    in_patient = InPatient(name, room_number)
    print("\n InPatient's's details")
    in_patient.patients_details()
    print(f"\n The InPatient's MRO\n{InPatient.__mro__}")

elif patient_type == "OutPatient":
    name = input("What's your name?: ")
    appointment_date = input("What's your appointment date?: ")

    out_patient = OutPatient(name, appointment_date)
    print("\n OutPatient's's details")
    out_patient.patients_details()
    print(f"\n The OutPatient's MRO\n{OutPatient.__mro__}")

else:
    print("Invalid patient type")






