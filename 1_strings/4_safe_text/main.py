import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    # разбиваем текст на предложения
    sentences = wrong_article.split('.\n')
    for i in range(len(sentences)):
        # убираем !
        sentences[i] = sentences[i].rstrip('!')
        # разворачиваем текст
        sentences[i] = sentences[i][::-1]
        # восстанавливаем cat
        sentences[i] = sentences[i].replace("WOOF-WOOF", "CAT")
        # первую букву в верхний регистр, остальные в нижний регистр
        sentences[i] = sentences[i].capitalize()

    return '.\n'.join(sentences)
