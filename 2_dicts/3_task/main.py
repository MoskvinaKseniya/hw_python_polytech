import re


def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    # оставляем цифры без символов
    number = re.sub(r'\D', '', phone_number)

    if len(number) == 11 and (number[0] == '8' or number[0] == '7'):
        # 89xxxxxxxxx или 79xxxxxxxxx
        formatted_phone_number = f'8 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:11]}'
    elif len(number) == 10 and number[0] == '9':
        # 9xxxxxxxxx
        formatted_phone_number = f'8 ({number[0:3]}) {number[3:6]}-{number[6:8]}-{number[8:10]}'
    else:
        formatted_phone_number = number

    return formatted_phone_number
