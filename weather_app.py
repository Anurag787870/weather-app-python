import requests

API_KEY="6e62504a33157ebc3625cebd7c60fcb3"
city=input("Enter the city name : ")
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response=requests.get(url)
data=response.json()

if response.status_code==200:
    print("City:", data["name"])
    print("Country:", data["sys"]["country"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Weather:", data["weather"][0]["main"])
    print("Description:", data["weather"][0]["description"])
    
else:
    print("Error",data["message"])