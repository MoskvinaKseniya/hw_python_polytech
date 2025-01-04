import requests
import sqlite3
from datetime import datetime, timezone, timedelta

API_key = "92bdbd47dd73e677a25fdb71a1e64554"  # API-ключ OpenWeatherMap
URL_OpenWeatherMap = "https://api.openweathermap.org/data/2.5/weather"
URL_Geolocation = "http://ip-api.com/json/"


def generate_app_response(data):
    """Формирование сообщения для пользователя с информацией о погоде"""
    # форматирование времени
    tz = timezone(timedelta(seconds=data["timezone"]))  # создание временной зоны с использованием смещения в секундах
    current_datetime = datetime.now(tz)
    formatted_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S%z")
    request_time = f"{formatted_time[:-2]}:{formatted_time[-2:]}"

    # остальную информацию достаем без форматирования
    city_name = data["name"]
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    wind_speed = data["wind"]["speed"]

    # формируем сообщение
    app_response = (
        f"\nТекущее время: {request_time}\n"
        f"Название города: {city_name}\n"
        f"Погодные условия: {weather_description}\n"
        f"Текущая температура: {temperature} градусов по цельсию\n"
        f"Ощущается как: {feels_like} градусов по цельсию\n"
        f"Скорость ветра: {wind_speed} м/с"
    )

    # добавление записи в историю
    add_to_history(request_time, city_name, weather_description, temperature, feels_like, wind_speed)

    return app_response


def get_weather_by_city_name(city_name):
    """Определить погоду по названию города"""
    try:
        params = {
            "q": city_name,
            "appid": API_key,
            "units": "metric",
            "lang": "ru"
        }
        # отправляем запрос на сервис
        response = requests.get(URL_OpenWeatherMap, params=params)

        # проверка на ошибки
        response.raise_for_status()
        weather_data = response.json()

        # вывод сообщения пользователю
        app_response = generate_app_response(weather_data)
        print(app_response)

    # обработка ошибок, связанных с запросом
    except requests.exceptions.RequestException as err:
        print("Возникла ошибка при попытке связаться с сервисом OpenWeatherMap.")
        print(err)
    # обработка ошибок, связанных с данными в ответе сервиса
    except KeyError:
        print("Ошибка: информация о погоде не найдена.")


def get_weather_by_geolocation():
    """Определить погоду по текущему местоположению пользователя"""
    try:
        params = {"lang": "ru"}
        # отправляем запрос на сервис
        response = requests.get(URL_Geolocation, params=params)

        # проверка на ошибки
        response.raise_for_status()
        location_data = response.json()
        city_name = location_data["city"]

        get_weather_by_city_name(city_name)

    # обработка ошибок, связанных с запросом
    except requests.exceptions.RequestException as err:
        print(f"Возникла ошибка при попытке определить ваше местоположение.")
        print(err)
    # обработка ошибок, связанных с данными в ответе сервиса
    except KeyError:
        print("Ошибка: информация о вашем текущем местоположении не найдена.")


def initialization_db():
    """Инициализируем базу данных"""
    conn = sqlite3.connect("weather_app_history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_time TEXT,
            city_name TEXT,
            weather_description TEXT,
            temperature REAL,
            feels_like REAL,
            wind_speed REAL
        )
    """)
    conn.commit()
    conn.close()


def add_to_history(request_time, city_name, weather_description, temperature, feels_like, wind_speed):
    """Добавление записи в историю."""
    conn = sqlite3.connect("weather_app_history.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO history (request_time, city_name, weather_description, temperature, feels_like, wind_speed)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (request_time, city_name, weather_description, temperature, feels_like, wind_speed))
    conn.commit()
    conn.close()


def get_history():
    """Вывод последних n записей из истории"""
    try:
        n = int(input("\nСколько последних запросов необходимо вывести? "))
        if n <= 0:
            print("Введите число больше 0.")

        conn = sqlite3.connect("weather_app_history.db")
        cursor = conn.cursor()
        cursor.execute("""
                SELECT request_time, city_name, weather_description, temperature, feels_like, wind_speed
                FROM history
                ORDER BY id DESC
                LIMIT ?
            """, (n,))
        history = cursor.fetchall()
        conn.close()

        if not history:
            return "История запросов пуста."

        print("\nИстория запросов:")
        for row in history:
            print("-" * 50)
            print(
                f"Текущее время: {row[0]}\n"
                f"Название города: {row[1]}\n"
                f"Погодные условия: {row[2]}\n"
                f"Текущая температура: {row[3]} градусов по цельсию\n"
                f"Ощущается как: {row[4]} градусов по цельсию\n"
                f"Скорость ветра: {row[5]} м/c\n"
            )

    except ValueError:
        print("Ошибка: введите целое число больше 0.")
