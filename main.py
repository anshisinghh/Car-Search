from user_inputs import get_user_inputs
from car_type import Type

def run():
    condition, year_min, model, make, exterior_color, city, state, price_max, category, fuel_type, mileage = get_user_inputs()

    try:
        t = Type(condition, year_min, model, make, exterior_color, city, state, price_max, category, fuel_type, mileage)
        t.get_car_data()
    except:
        print("Failed")
    
if __name__ == '__main__':
    run()
