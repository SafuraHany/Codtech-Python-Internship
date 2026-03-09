import requests
import matplotlib.pyplot as plt

API_KEY = "8c3fdd0c333c50d280e2442829d25f8f"
city = "Hyderabad"

url = f"http://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=8c3fdd0c333c50d280e2442829d25f8f&units=metric"

response = requests.get(url)
data = response.json()

print(data)   # this helps us see what the API returned

if "main" in data:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    labels = ["Temperature", "Humidity", "Pressure"]
    values = [temperature, humidity, pressure]

    plt.bar(labels, values)
    plt.title("Weather Data for Hyderabad")
    plt.ylabel("Values")
    plt.show()

else:
    print("API Error:", data)