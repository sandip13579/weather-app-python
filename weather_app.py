import requests

city = input("Enter a city:")

API_key = "7969406a52fb3b5f29513d61eebc57bd"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

r = requests.get(url)   
data = r.json()



if data['cod'] != 200:
    print("City Not found")
else:
    temp = data['main']['temp']-273.15
    humidity = data['main']['humidity']
    weather = data['weather'][0]['main']
    weather_description = data['weather'][0]['description']
    print("City:",city)
    print(f"Temperature:{temp:.2f} C")
    print(f"Humidity:{humidity}%")
    print("Weather:",weather)
    print("Weather Description:",weather_description)