import requests

API_KEY = "de344ea2bc73b33e12d215c4b748b083"
ZIP_CODE = '110001'
COUNTRY_CODE = 'IN'

URL = 'http://api.openweathermap.org/geo/1.0/zip?zip={},{}&appid={}'.format(ZIP_CODE,COUNTRY_CODE,API_KEY)

response = requests.get(URL)
data = response.json()
lat = data['lat']
lon = data['lon']    

def Get_Weather():
    Main_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, API_KEY)
    Response = requests.get(Main_URL)
    Data = Response.json()

    if Data['cod'] == 200:
        Weather_Info = {
            'City': data['name'],
            'Latitude': (lat),
            'longitude': (lon),
            'Temperature(Celsius)': Data['main']['temp'],
            'Feels Like(Celsius)': Data['main']['feels_like'],
            'Description': Data['weather'][0]['description'],
            'Humidity (%)': Data['main']['humidity'],
            'Wind Speed (m/s)': Data ['wind']['speed'],
        }
        return Weather_Info
    else:
        print("Error")

def main():
    Weather_Data = Get_Weather()
    print(Weather_Data)

main()
