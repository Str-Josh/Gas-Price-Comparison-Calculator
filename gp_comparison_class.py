# python program to test if it's cheaper to travel for gasoline

class CalculateGasPrice(object):
    def __init__(self, mpg, tank_capacity, required_gas, current_city_price,
                 comparer_city_price, mileage_distance_bw_cities):
        self.mpg = mpg
        self.tank_capacity = tank_capacity
        self.required_gas = required_gas
        self.current_city_price = current_city_price
        self.comparer_city_price = comparer_city_price
        self.mileage_distance_bw_cities = mileage_distance_bw_cities

        self.travel_gas_loss = self.mileage_distance_bw_cities / self.mpg

        # calculated results
        self.travel_required_gas = self.required_gas + self.travel_gas_loss
        self.pay_price_travel_city = round((self.travel_required_gas * self.comparer_city_price), 2)
        self.pay_price_current_city = round((self.required_gas * self.current_city_price), 2)

    def calculate_pay_comparison(self):
        print(f"\nif you travel to fill you will pay: {self.pay_price_travel_city}\n")
        print(f"if you fillup in current city you should pay: {self.pay_price_current_city}\n")
        
        save_lose_decision = None
        diff_bw_prices = (self.pay_price_current_city - self.pay_price_travel_city)

        if diff_bw_prices > 0:
            save_lose_decision = "SAVE"
        elif diff_bw_prices < 0:
            save_lose_decision = "LOSE"
        else:
            save_lose_decision = "NIETHER SAVE NOR LOSE"
            
        print(f"\nYou will {save_lose_decision} ${abs(round(diff_bw_prices, 2))} if you travel for gas")


cur_city_gp = float(input("Please enter the price of gas in your current city: "))
trav_city_gp = float(input("Now please enter the price of gas in the traveling city: "))

# tank_cap = float(input("Please enter the tank capacity of your vehicle: "))
city_dist = float(input("Please enter the distance between the cities for travel: "))

if cur_city_gp == 0 and trav_city_gp == 0 and city_dist == 0:
    v1 = CalculateGasPrice(22, 20, 19, 4.6, 4.2, 16)
    v1.calculate_pay_comparison()
    print("----------")
    v2 = CalculateGasPrice(22, 20, 19, 5.19, 5.9, 16)
    v2.calculate_pay_comparison()

else:
    # parameter list: mpg, tank capacity, required gas, ..., distance b/w
    dummy_vars = [22, 20, 19]

    comparison_price1 = CalculateGasPrice(dummy_vars[0], dummy_vars[1], 
                                          dummy_vars[2], cur_city_gp, 
                                          trav_city_gp, city_dist)

    comparison_price1.calculate_pay_comparison()


"""

# ask if the user would like to account for round trip
acct_round_trip = str(
    input("Would you like to account for round trip? (Y/N)\n\t>> "))
if acct_round_trip.upper() == 'Y':
    pass
elif acct_round_trip.upper() == 'N':
    quit()
else:
    print("What tf did you say to me!?!?!? Try again skank")

"""
