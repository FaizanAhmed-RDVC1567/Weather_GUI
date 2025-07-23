import tkinter as tk
from services.weather_scraper import get_weather_data


class WeatherApp:
    def __init__(self):
        self.root = tk.Tk("WeatherGUI")
        self.root.title("Weather Info")
        self.root.geometry("400x300")

        self.city_entry = tk.Entry(self.root, width=30)
        self.city_entry.pack(pady=10)

        self.search_button = tk.Button(self.root, text="Get Weather", command=self.display_weather)
        self.search_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", wraplength=350, justify="left")
        self.result_label.pack(pady=10)

    def display_weather(self):
        city = self.city_entry.get()
        weather_info = get_weather_data(city)
        self.result_label.config(text=weather_info)

    def run(self):
        self.root.mainloop()