import os
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    employees_info = get_employees_info()
    parsed_employees_info = []

    # Ваш код ниже
    # допустимые ключи
    keys = ['id', 'name', 'last_name', 'age', 'salary', 'position']

    for line in employees_info:
        elements = line.split()
        parsed_line = {}

        for i in range(0, len(elements), 2):
            key = elements[i]
            if key in keys:
                if key == keys[0] or key == keys[3]:
                    parsed_line[key] = int(elements[i+1])
                elif key == keys[4]:
                    parsed_line[key] = Decimal(elements[i+1])
                else:
                    parsed_line[key] = elements[i+1]

        parsed_employees_info.append(parsed_line)

    return parsed_employees_info
