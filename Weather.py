import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 300
WIDTH = 400

def format_response(weather):
    try: 
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperture (C): %s' %(name, desc ,temp)
    except:
        final_str = 'Small Problem Retrieving that Infomation'
    
    return final_str

def get_weather(city):
    weather_key = '85a4e70fbd45c03f76d04a489291730a'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file='landscape.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='#abcdef', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(upper_frame, font=40)
entry.place(relwidth=0.65, relheight=1)

btn = tk.Button(upper_frame, text='Get Weather', font=40, command=lambda: get_weather(entry.get()))
btn.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#abcdef', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()