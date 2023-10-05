import requests
from datetime import datetime as dt

# Global variables
API_key = "9d8f995de0de6283e9cbb0e48d00f94b"
data_file = open ("data.txt", "a")

# Gets the desired news data based off user input
def get_weather(city_name, api_key = API_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"
    req = requests.get(url)
    contents = req.json()

    for data in contents['list']:
        # add city, time, temperature, and condition to .txt file
        time_stamp = dt.fromtimestamp(data['dt']) # Convert timestamp to date
        temp = round(9 / 5 * (float(data['main']['temp']) - 273.15) + 32) # Kelvin to Fahrenheit
        condition = data['weather'][0]['description']
        data_file.write(f"{city_name}   {time_stamp}   {temp}   {condition}\n") # Write data to .txt file
    #data_file.close()
    data_file.read()

def __main__():
    get_weather(city_name= "tyler")
    


__main__()