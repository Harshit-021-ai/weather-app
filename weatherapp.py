import requests

API_KEY = "de344ea2bc73b33e12d215c4b748b083"
ZIP_CODE = '110001'
COUNTRY_CODE = 'IN'

URL = 'http://api.openweathermap.org/geo/1.0/zip?zip={},{}&appid={}'.format(ZIP_CODE,COUNTRY_CODE,API_KEY)

response = requests.get(URL)
Location_Data = response.json()
lat = Location_Data['lat']
lon = Location_Data['lon']    

def Get_Weather():
    Main_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, API_KEY)
    Response = requests.get(Main_URL)
    Weather_Data = Response.json()

    if Weather_Data['cod'] == 200:
        Weather_Info = {
            'City': Location_Data['name'],
            'Latitude': (lat),
            'Longitude': (lon),
            'Temperature (Celsius)': round(Weather_Data['main']['temp'] - 273.15, 2),
            'Feels Like (Celsius)': round(Weather_Data['main']['feels_like'] - 273.15, 2),
            'Description': Weather_Data['weather'][0]['description'],
            'Humidity (%)': Weather_Data['main']['humidity'],
            'Wind Speed (m/s)': Weather_Data ['wind']['speed'],
        }
        return Weather_Info
    else:
        print("I Think Something Is Wrong With Your API")

def main():
    Weather_Data = Get_Weather()
    print(Weather_Data)

main()

def main():
    Weather_Data = Get_Weather()
    print(Weather_Data)

main()
