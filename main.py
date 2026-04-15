import requests
import tkinter as tk
from ttkbootstrap import Style

api_key = '8dd33acbccf25bde30aa84b56753f7bf'

root = tk.Tk()
root.title("Weather App")
style = Style(theme='united')
root.geometry("400x250")

label = tk.Label(root, text="Enter the city name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label_country = tk.Label(root, text="")
label_country.pack()
label_timezone = tk.Label(root, text="")
label_timezone.pack()
label_weather = tk.Label(root, text="")
label_weather.pack()
label_temperature1 = tk.Label(root, text="")
label_temperature1.pack()
label_temperature2 = tk.Label(root, text="")
label_temperature2.pack()
label_pressure = tk.Label(root, text="")
label_pressure.pack()
label_humidity = tk.Label(root, text="")
label_humidity.pack()

def get_weather():
    user_input = entry.get()
    weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric')
    if weather_data.status_code == 200:
        data = weather_data.json()
        country = data['sys']['country']
        timezone = data['timezone']
        weather = data['weather'][0]['description']
        temperature1 = data['main']['temp']
        temperature2 = data['main']['feels_like']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']

        label_country.config(text=f"Country: {country}")
        label_timezone.config(text=f"Timezone: {timezone}")
        label_weather.config(text=f"Weather: {weather}")
        label_temperature1.config(text=f"Temperature: {temperature1}°C")
        label_temperature2.config(text=f"Feels Like: {temperature2}°C")
        label_pressure.config(text=f"Pressure: {pressure} hPa")
        label_humidity.config(text=f"Humidity: {humidity}%")

        bg='#ADD8E6'
        if temperature1 < 10 :
            bg ='#ADD8E6'
        elif 10 <= temperature1 <= 25 :
            bg='#90EE90'
        elif temperature1 > 25:
            bg= '#FFB347'

       
        root.configure(bg=bg)
        label.config(bg=bg)
        label_country.config(bg=bg)
        label_timezone.config(bg=bg)
        label_weather.config(bg=bg)
        label_temperature1.config(bg=bg)
        label_temperature2.config(bg=bg)
        label_pressure.config(bg=bg)
        label_humidity.config(bg=bg)
    else:
        label_country.config(text="City not found. Please try again.")

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

root.mainloop()