from weather_functions import get_weather_by_city_name, get_weather_by_geolocation, get_history, initialization_db


# точка входа
if __name__ == "__main__":
    # инициализируем базу данных
    initialization_db()

    print("Добро пожаловать в приложение прогноза погоды!")

    while True:
        print("\n", "*" * 50)
        print("Доступные команды:\n"
              "1. определить погоду по названию города\n"
              "2. определить погоду по моему местоположению\n"
              "3. посмотреть историю запросов\n"
              "4. завершить работу")

        try:
            action_number = int(input("\nВведите номер команды: "))
            if action_number == 1:
                city_name = input("\nВведите название города: ").strip()
                if len(city_name) == 0:
                    print("\nОшибка: название города не может быть пустым.")
                    continue
                get_weather_by_city_name(city_name)

            elif action_number == 2:
                get_weather_by_geolocation()

            elif action_number == 3:
                get_history()

            elif action_number == 4:
                print("\nРабота программы завершена.")
                break

            else:
                print("\nОшибка: введите номер команды от 1 до 4.")

        except ValueError:
            print("\nОшибка: введите корректный номер команды - число от 1 до 4.")
