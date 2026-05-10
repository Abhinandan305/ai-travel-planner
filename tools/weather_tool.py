import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    try:

        response = requests.get(url)

        return response.json()

    except Exception as e:

        print(f"Weather API Error: {e}")

        return {}