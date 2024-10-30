def encode_text(text: str) -> str | None:
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

    # обратный словарь
    char_on_keypad = {}
    for key, chars in keypad.items():
        for i, char in enumerate(chars):
            # Каждый символ соответствует нажатиям key * (i + 1)
            char_on_keypad[char] = key * (i + 1)

    result = []

    for char in text.lower():
        if char in char_on_keypad:
            result.append(char_on_keypad[char])
        else:
            return None

    return ' '.join(result)
