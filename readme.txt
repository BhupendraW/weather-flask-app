# 🌤️ Weather App using Flask

A simple and elegant weather web app built with **Flask** that fetches live weather data using the **OpenWeatherMap API**. Users can enter any city name to get real-time temperature, humidity, weather description, and dynamic background images based on the weather condition.

---

## 🚀 Features

- 🌍 Enter any city name and get current weather data
- 🌡️ Displays temperature (°C), humidity, and weather condition
- 🌅 Weather-based background image changes dynamically
- ⚠️ Shows error if city is not found
- 🔄 Fully responsive and minimal design

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask** (Backend Framework)
- **Jinja2** (Template Engine)
- **HTML/CSS** (Frontend)
- **Requests** (Python library to fetch API)
- **OpenWeatherMap API**

---

## 🔑 OpenWeatherMap API Setup

To fetch live weather data, we use the **OpenWeatherMap API**. Follow these steps to get your free API key:

### ✅ Step-by-Step:

1. Go to 🌐 https://home.openweathermap.org/users/sign_up  
2. Create a free account and verify your email
3. After login, go to your profile → **"API Keys"** section  
4. Copy the **default API key** (or generate a new one)
5. Paste it into your `app.py`:

```python
API_KEY = 'your_api_key_here'




⏳ Note:
It may take 5–10 minutes after signup for your API key to start working.

