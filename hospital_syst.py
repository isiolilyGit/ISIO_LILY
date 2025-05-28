#Method Overloading
class Patient:
    def __init__(self, patient_name):
        self.patient_name = patient_name
    def payment(self, *args):
        
        if len(args) == 1:
            consultation_fee = args[0]
            print(f"Full_cost without treatment  for {self.patient_name}: {consultation_fee}") 
        
        elif len(args) == 2:
            consultation_fee, treatment_cost = args
            full_cost =  consultation_fee + treatment_cost
            print(f"Full cost with treatment {self.patient_name} is: {full_cost} ")

        else:
            return 0

patient = Patient("Ime Lily")
patient.payment(100)
patient.payment(100, 300)


