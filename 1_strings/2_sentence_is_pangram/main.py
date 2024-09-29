"""
Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""
import string


def is_sentence_is_pangram(sentence: str) -> bool:
    # буквы алфавита
    alphabet = string.ascii_lowercase
    # буквы в предложении
    sentence = sentence.lower()
    letters = ""
    for i in sentence:
        if i not in letters:
            letters = letters + i
    letters = ''.join(sorted(letters))

    return alphabet == letters


