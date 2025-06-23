import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    cityname = city_entry.get().strip()
    if not cityname:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    apiKey = "7040ea904442a45d6950ba584410ce59"  
    baseURL = "http://api.openweathermap.org/data/2.5/weather?q="
    completeURL = baseURL + cityname + "&appid=" + apiKey

    try:
        response = requests.get(completeURL)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            wind = data["wind"]
            temperature_k = main["temp"]
            temperature_c = round(temperature_k - 273.15, 2) 
            humidity = main["humidity"]
            wind_speed = wind["speed"]
            weather_desc = data["weather"][0]["description"]

            weather_report = (
                f"Weather in {cityname}:\n"
                f"Temperature: {temperature_c}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s\n"
                f"Description: {weather_desc.capitalize()}"
            )

            result_label.config(text=weather_report)
        else:
            result_label.config(text="City not found.")
    except Exception as e:
        result_label.config(text="Error fetching data. Please check your internet or API key.")

window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")
window.resizable(False, False)

tk.Label(window, text="Weather Report", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(window, text="Enter City Name:").pack()
city_entry = tk.Entry(window, width=30)
city_entry.pack(pady=5)

tk.Button(window, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), justify="left", wraplength=350)
result_label.pack(pady=10)

window.mainloop()
