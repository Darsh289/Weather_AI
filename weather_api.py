import requests

API_KEY = "07e0b894a36d48106b01781b07ace508"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None

    weather = {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "condition": data["weather"][0]["main"]   # ⭐ NEW
    }

    return weather