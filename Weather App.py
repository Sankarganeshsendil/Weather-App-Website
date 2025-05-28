import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather_info = (
            f"City: {data['name']}, {data['sys']['country']}\n"
            f"Temperature: {data['main']['temp']} °C\n"
            f"Weather: {data['weather'][0]['description'].capitalize()}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Wind Speed: {data['wind']['speed']} m/s"
        )
    except Exception as e:
        weather_info = f"Error: {e}"

    result_label.config(text=weather_info)

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
root.config(bg="lightblue")

tk.Label(root, text="Enter City Name:", bg="lightblue", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 10), justify="left")
result_label.pack(pady=10)

root.mainloop()

