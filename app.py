from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = 'Your API KEY'  # Your OpenWeatherMap API Key

def get_background(description):
    description = description.lower()
    if "clear" in description:
        return "https://images.unsplash.com/photo-1501973801540-537f08ccae7b"
    elif "cloud" in description:
        return "https://images.unsplash.com/photo-1499346030926-9a72daac6c63"
    elif "rain" in description or "drizzle" in description:
        return "https://images.unsplash.com/photo-1505245208761-ba872912fac0"
    elif "thunderstorm" in description:
        return "https://images.unsplash.com/photo-1500674425229-f692875b0ab7"
    elif "snow" in description:
        return "https://images.unsplash.com/photo-1608889175117-415927122d0e"
    else:
        return "https://source.unsplash.com/1600x900/?weather"

def error_background():
    return "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzg5amFsMHJua2VmcjMzODJ6M3g0Z2JndmdmdDNkNjlybTRtYWkwMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nVTa8D8zJUc2A/giphy.gif"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    background_url = "https://source.unsplash.com/1600x900/?weather"

    if request.method == 'POST':
        city = request.form.get('city').strip()
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                description = data['weather'][0]['description']
                background_url = get_background(description)

                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': data['wind']['speed'],
                    'description': description,
                    'icon': data['weather'][0]['icon'],
                    'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                    'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
                    'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                }
            else:
                weather_data = {'error': '❌ City not found. Please enter a valid city name.'}
                background_url = error_background()

    return render_template('index.html', weather=weather_data, bg=background_url)

if __name__ == '__main__':
    app.run(debug=True)
