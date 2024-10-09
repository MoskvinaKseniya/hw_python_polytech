import re
from collections import Counter


def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    # разбиваем текст на слова
    words = re.findall(r'\b\w{3,}\b', text.lower())
    # подсчитываем количество вхождений каждого слова
    word_counts = Counter(words)
    # сортировка: первый приоритет по количеству вхождений, второй по алфавиту
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    # возвращаем первые 10
    most_common = dict(sorted_words[:10])
    return most_common
