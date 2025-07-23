import requests
from bs4 import BeautifulSoup


def get_weather_data(city):
    try:
        url = f"https://www.weather-forecast.com/locations/{city.replace('', '-')}/forecasts/latest"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        forecast = soup.find("span", class_="phrase")
        if forecast:
            return f"Weather in {city}:\n{forecast.text}"
        else:
            return "Weather information not found."
    except Exception as e:
        return f"Error fetching weather data: {e}"
