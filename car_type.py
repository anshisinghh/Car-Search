import requests
import json
import shutil
from PIL import Image


class Type:
    def __init__(self, condition, year, model, make, color, city, state, price_max, category, fuel_type, mileage):
        try:
            apikey = "ZrQEPSkKYW5zaGlzaW5naDczMEBnbWFpbC5jb20="
            url = 'https://auto.dev/api/listings?apikey=' + apikey

            self._final_url = url + '&limit=1'

            if make != None:
                self._final_url += '&make=' + make
            if model != None:
                self._final_url += '&model=' + model
            if year != None:
                self._final_url += '&year_min=' + year
            if color != None:
                self._final_url += '&exterior_color[]=' + color
            if city != None:
                self._final_url += '&city=' + city
            if state != None:
                self._final_url += '&state=' + state
            if price_max != None:
                self._final_url += '&price_max=' + price_max
            if category != None:
                self._final_url += '&category=' + category
            if fuel_type != None:
                self._final_url += '&fuel_type=' + fuel_type
            if mileage != None:
                self._final_url += '&mileage=' + mileage
    
            response = requests.request("GET", self._final_url)
            self._data = json.loads(response.content)
        except:
            print('API unavailable')


    def get_car_data(self):
        if self._data['records'] == []:
            print('No matches found.')
        else:
            records = self._data['records'][0]
            print('\nCongrats, you have found a match!')
            car_type = 'The car found is a ' + (str(records['year'])).strip() + ' ' + (records['make']).strip() + ' ' + (records['model']).strip() + '.'
            print(car_type)
            print('Condition:', records['condition'], '\nColor:', records['displayColor'] , '\nMileage:', records['mileage'], '\nPrice:', records['price'])

            response = requests.get(records['primaryPhotoUrl'], stream=True)
            with open('img.png', 'wb') as file:
                shutil.copyfileobj(response.raw, file)
            del response

            img = Image.open('img.png')
            img.show()
            location = (records['city']).strip() + ', ' + (records['state']).strip()
            print('Nearest Dealer:', records['dealerName'], 'located in', location, '\nLink to Website:', records['clickoffUrl'], '\n')
        


