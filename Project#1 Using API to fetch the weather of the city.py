import requests

def kelvin_to_celsius(kelvin):
    number=kelvin-273.15
    formatted_number = "{:.2f}".format(number)
    return formatted_number

import requests

def fetch_temperature():
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key = '131f26bd6d1791a42ce08b123506ff85'
    print('--------------------------------------------------------------------')
    city = input("Please Enter Your valid City_Name :")

    params = {'q': city, 'appid': api_key}

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        print('Result :-')
        print("         The temprature in ",city," is ",kelvin_to_celsius(temperature),"℃")
    else:
        print("Error:", response.status_code)

fetch_temperature()
print('--------------------------------------------------------------------')
