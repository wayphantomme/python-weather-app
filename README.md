# 📌 **Python Weather App**

A simple command-line weather application built with Python that fetches real-time weather data from the **OpenWeatherMap API**.
You can input any city name and instantly get the weather condition, temperature, date, and other useful info.

---

## 🚀 Features

* Get real-time weather for any city
* Displays:

  * Current date
  * Weather status (Clear, Clouds, Rain, etc.)
  * Temperature (°F or °C, based on your code)
* Simple, lightweight, and beginner-friendly
* Uses the `requests` library
* Runs inside a Python virtual environment

---

## 🧪 Example Output

```
Enter city: Los Angeles
Date: Monday, November 24, 2025
The weather in Los Angeles is: Clear
The temperature in Los Angeles is: 59°F
```

---

## 🛠️ Installation

### 1. Clone this repository

```
git clone https://github.com/wayphantomme/python-weather-app.git
cd python-weather-app
```

### 2. Create and activate virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install requests
```

---

## 🔑 Setup API Key

This project uses the **OpenWeatherMap API**.

1. Go to [https://openweathermap.org/api](https://openweathermap.org/api)
2. Create a free account
3. Get your API key
4. Open `app.py` and replace:

```python
api_key = "YOUR_API_KEY_HERE"
```

---

## ▶️ How to Run

```
python app.py
```

Then enter any city name when prompted.

---

## 📂 Project Structure

```
python-weather-app/
│
├── app.py
├── README.md
└── .gitignore
```

---

## ❗ Notes

* Do **not** upload `.venv` to GitHub
* Make sure your API key is **not exposed** in public repos
* If using this repo publicly, consider using environment variables

---

## 📜 License

This project is free to use for learning and experimentation.
