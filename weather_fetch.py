import requests

BASE_URL="http://api.openweathermap.org/data/2.5/weather"
API_KEY="your api key here"

def get_data(city_name):
     parameters={
          'q':city_name,
          'appid': API_KEY,
        'units': 'metric'
     }
     try:
          response=requests.get(BASE_URL,params=parameters)
          if response.status_code==200:
               data=response.json()
               return data
          elif response.status_code==404:
               print("error data not found")
               return None
          else:
               print("error ")
               return None
     except requests.exceptions.RequestException as e:
          print(f"connection not found: {e}")
          return None
def display(city_name):
     weather=get_data(city_name)
     if weather:
          temp_celsius =weather['main']['temp']
          humidity=weather['main']['humidity']
          description=weather['weather'][0]['description'].capitalize()     

          print("-" * 40)
          print(f"Weather Report for: {city_name.upper()}")
          print("-" * 40)
          print(f"Temperature: {temp_celsius :.1f}°C")
          print(f"Condition:   {description}")
          print(f"Humidity:    {humidity}%")
          print("-" * 40)
     else:
        print("Could not display weather data.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    display(city)
