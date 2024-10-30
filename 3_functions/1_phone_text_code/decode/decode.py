def decode_numbers(numbers: str) -> str | None:
    # словарь
    keypad = {
        '1': '.,?!:;',
        '2': 'абвг',
        '3': 'дежз',
        '4': 'ийкл',
        '5': 'мноп',
        '6': 'рсту',
        '7': 'фхцч',
        '8': 'шщъы',
        '9': 'ьэюя',
        '0': ' '
    }

    # Разделяем строку на части по пробелам
    elements = numbers.split()

    result = []

    for element in elements:
        # первая цифра - клавиша
        key = element[0]
        if element[0] not in keypad or len(set(element)) > 1:
            return None

        # по длине находим символ
        length = len(element)

        # количество нажатий не превышает количество доступных символов для этой цифры
        if length > len(keypad[key]):
            return None

        # Выбираем соответствующую букву
        char = keypad[key][length - 1]
        result.append(char)

    return ''.join(result)
