class Transport:
    #Calculating the total fare for each vehicle type
    #Constant rate of 0.5
    print(f"  The transport fares")
    def calculate_fare(self, distance, *args):
        distance = float(input("What's the distance: "))
        if len(args) == 0:
            total_fare=  distance * 0.5
            print(f"Fare based on distance only: shs{total_fare:2f}")
        
        elif len(args) == 1:
            no_of_passengers = args[0]
            no_of_passengers = int(input("How many passengers are boarding: "))
            total_fare = distance * 0.5 * no_of_passengers
            print(f"Fare based on distance and number of passengers: shs{total_fare:.2f}")
        
        else:
            no_of_passengers, luggage_weight = args
            luggage_weight = float(input("What's the weight of your luggage: "))
            total_fare = distance * 0.5 * no_of_passengers + luggage_weight
            print(f"fare with luggage weight included: shs{total_fare:.2f}")
            

trans_syst = Transport()
trans_syst.calculate_fare(6) #Calculates fare based on distance only
trans_syst.calculate_fare(6, 7) #Distance and number of passengers
trans_syst.calculate_fare(6, 7, 9) #Distance, number of passengers and luggage weight

   
        
   
    