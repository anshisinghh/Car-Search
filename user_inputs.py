def get_user_inputs():
    print('Looking to buy a car? We will search through thousands of cars on sale and find the one best suited to your needs.\n')

    user_input = (input('Condition of car (i.e. used, new, n/a, etc.)?\n')).lower()
    condition = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        condition = None

    user_input = (input('Minimum year of car?\n')).lower()
    year_min = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        year_min = None

    user_input = (input('Make of car (i.e. Honda, Acura, n/a, etc.)?\n')).capitalize()
    make = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        make = None

    user_input = (input('Model of car (i.e. Civic, A4, n/a)?\n')).capitalize()
    model = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        model = None

    user_input = (input('Color of car (i.e. grey, black, n/a, etc.)?\n')).lower()
    exterior_color = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        exterior_color = None
    
    user_input = input('City and state of car location (i.e. Irvine, CA; n/a; etc.)?\n')
    if user_input == 'n/a':
        city = None
        state = None
    else:
        location = user_input.split(',')
        city = location[0].replace(' ', '%20')
        state = location[1].upper().strip()
    
    user_input = (input('Maximum price of car (i.e. 25000, n/a, etc.)?\n')).lower()
    price_max = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        price_max = None

    user_input = (input('Category of car (i.e. family, hybrid, sport, large, n/a, etc.)?\n')).lower()
    category = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        category = None

    user_input = (input('Fuel type of car (i.e. gasoline, electric, n/a, etc.)?\n')).lower()
    fuel_type = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        fuel_type = None

    user_input = (input('Maximum mileage of car (i.e. 81000, n/a, etc.)?\n')).lower()
    mileage = user_input.replace(' ', '%20')  
    if user_input == 'n/a':
        mileage = None


    return condition, year_min, model, make, exterior_color, city, state, price_max, category, fuel_type, mileage

