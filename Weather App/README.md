# The Weather App

This application uses OpenWeatherMap's API to obtain weather forecast data to display the current weather information based on a user input.

#
**Languages Used**

- Python

#
**Packages Used**

- API for OpenWeatherMap
- Requests

You will need to sing up for API Key and make a connection to the API using the Requests library. Once the request connection is made to the OpenWeather API, the App will display whether the connection is success or not.

#
**How the App Works**

First, the App will ask a user for a zip code or city, and then the App will use the zip code or city name to fetch weather forecast data from OpenWeatherMap. It will, then, display the weather forecast with the following information:

- Current condition
- Current temperature
- Feels-like temperature
- Temperature in Celsius
- Wind Speed
- Current Humidity
- Description of clouds
- Min Temperature
- Max Temperature
- Pressure

The program is written to show if the user has entered valid input. Otherwise, it will display the error message and ask the user to re-enter valid input. After using the App, the user can quit the program.

#
**Reference**
OpenWeather API, https://openweathermap.org/api.
