# DSC 510
# Week 12
# Programming Assignment Week 12 - Final Term Project
# This week's program requests Openweather API in Python to build a real life weather app.
# Author: Phil Han
# 06/05/21


import requests         # requests connection to openweather api
from simple_colors import *  # import simple colors to print in bold c
#from pprint import pprint

# global URL with the API key to request the data from the openweather API
API_key = "3bb5c98efaef84f415723167fee35118"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def weather_city(city):         # get weather by an input with city name

    try:
        # takes input for city name and state code
        city_name = input("Enter a city name: ")
        state_code = input("Enter a state abbreviation: ")
        state = str(state_code)
        Final_url = base_url + "q=" + city_name + ',' + state_code + ','+'US&units=metric' + "&appid=" + API_key
        Final_url = base_url + "q=" + city_name + ',' + state_code + ','+'US&units=imperial' + "&appid=" + API_key

        # response expression/error handling to check connection status
        response = requests.get(Final_url)
        weather_data = requests.get(Final_url).json()   # requests connection to API data
        try:
            weather_data = requests.get(Final_url).json()
        except requests.ConnectionError as e:
            print('Connection Failure : ', str(e))
        except requests.exceptions.HTTPError as e:
            print('Connection Failure : ', str(e))

        # displays city and state code
        city_name = weather_data['name']
        state_code = weather_data['sys']['country']
        print(green('\nLocation : ', 'bold') + blue(city_name, 'bold') + blue(',', 'bold'), blue(state.upper(), 'bold'))
        if response.status_code == 200:
            print('Connection Status: ' + green('SUCCESS!', 'bold'))
        elif response.status_code == 404:
            print(red('Connection Not Found.', 'bold'))
        current_weather(weather_data)
    except KeyError:
        print(red("Error: City is not found.  Please enter a valid city name and state code! ", 'bold'))
        weather_city(city)



def weather_zip(zip):       # get weather by an input with zip code

    try:
        # takes input for zip code to check the weather
        zip_code = input("Enter a 5 digit zip code: ")
        zip = int(zip_code)
        Final_url = base_url + "zip=" + zip_code + ",us&appid=" + API_key + '&units=imperial'

        # response expression/error handling to check connection status
        response = requests.get(Final_url)
        try:
            weather_data = requests.get(Final_url).json()       # requests connection to openweather api
        except requests.ConnectionError as e:
            print('Connection Failure : ', str(e))
        except requests.exceptions.HTTPError as e:
            print('Connection Failure : ', str(e))
        zip_code = weather_data['name']
        print('\nZip Code :', zip)
        print('City Name :', green(zip_code, 'bold'))
        if response.status_code == 200:
            print('Connection Status: ' + green('SUCCESS!', 'bold'))
        elif response.status_code == 404:
            print(red('Connection Not Found.', 'bold'))
        current_weather(weather_data)
    except KeyError:
        print(red("Error:  Invalid zip code. Please enter a valid zip code! ", 'bold'))
        weather_zip(zip)
    except ValueError:
        print(red("Error:  Invalid zip code. Please enter a valid zip code! ", 'bold'))
        weather_zip(zip)



def current_weather(weather_data):          # display current weather with detailed up-to-date info by city or zip code

    condition = weather_data['weather'][0]['main']  # display current condition

    temp = weather_data['main']['temp']     # display current temp in °F

    feels_like = weather_data['main']['feels_like'] # display feels like temp in °F

    temp_celsius = float((temp - 32)*(5/9))     # display temp in celsius

    wind_speed = weather_data['wind']['speed']      # display wind speed (mph)

    current_humidity = weather_data['main']['humidity']     # display humidity

    cloud_describe = weather_data['weather'][0]['description']      # display cloud cover

    min_temp = weather_data['main']['temp_min']             # display min temp °F

    max_temp = weather_data['main']['temp_max']             # display max temp °F

    pressure = weather_data['main']['pressure']             # display pressure

    # used Simple_Colors package to print out the output in simple colors in bold
    print(blue('\nCondition : ', 'bold'), condition.upper())
    print(green('Temperature : ', 'bold'), temp,'°F')
    print(red('Feels like : ', 'bold'), feels_like, '°F')
    print(yellow('Temperature Celsius : ', 'bold'), round(temp_celsius, 2),'°C')
    print(blue('Wind Speed : ', 'bold'), wind_speed,'mph')
    print(green('Current Humidity : ', 'bold'),current_humidity,'%')
    print(red('High Temp : ', 'bold'), max_temp, '°F')
    print(yellow('Low Temp : ', 'bold'),min_temp,'°F')
    print(green('Pressure :', 'bold'), pressure,'hPa')
    print(blue('Cloud Cover : ', 'bold'), cloud_describe.upper())
    print('\n')
    #pprint(weather_data)  # print json data to look at keys/values when double-checking but commented out.



def main():     # main function to take an option to run the weather app by city name or zip code or quit
    print(blue(" Welcome to BestVue Weather App! ".center(58, '#'),'bold'))
    print(blue("\nTo check the current weather, please choose the following: ", 'bold'))
    while True:
        # the URL for Openweather API
        API_key = "3bb5c98efaef84f415723167fee35118"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # gives the user options to run the weather app by city name, zip code, or quit
        choice = input("Select:'C' for a city name : 'Z' for Zip Code : 'Q' to quit the App: ")
        city = None
        zip = None
        response = None

        try:
            if choice == 'C' or choice == 'c':
                city_name = str()
                weather_city(city)

            elif choice == 'Z' or choice == 'z':
                zip_code = str(int)
                weather_zip(zip)


            elif choice == 'Q' or choice == 'q':
                print(blue(' Thanks for using this program! '.center(58, '#'), 'bold'))
                break

            elif choice != 'C' or 'Z' or 'Q':
                print(red("Error: Please enter a valid input to check the weather! ", 'bold'))
        except:
            print(red("Error: Connection Not Found or Invalid Input: Please try again! ", 'bold'))


    else:
        print("Thanks for using our BestVue Weather App!".center(40, '#'))
        

if __name__ =="__main__":
    main()

