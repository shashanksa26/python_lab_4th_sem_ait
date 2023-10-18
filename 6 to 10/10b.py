import requests
# Enter the API key you got from the OpenWeatherMap website
api_key = "d2e84b1c0ccef0f0ff660b262c7488ea"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# This is to complete the base_url, you can also do this manually to
# checkout other weather data available
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# get method of requests module
# return response object
response = requests.get(complete_url)
# json method of response object
# convert json format data into
# python format data
x = response.json()
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
# store the value of "main"
# key in variable y
    y = x["main"]
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    z = x["weather"]
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
    # print following values
    print(" Temperature (in kelvin unit) = " +
    str(current_temperature) +"\n description = " +str(weather_description))
else:
    print(" City Not Found ")