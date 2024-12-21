import os.path
from datetime import datetime, timezone


class TxtStorage:
    def __init__(self, path: str, buffer_limit: int):
        """
        - path: путь к файлу для хранения данных.
        - buffer_limit: размер буфера перед записью в файл.
        - buffer: хранение метрик перед записью
        """
        self.path = path
        self.buffer_limit = buffer_limit
        self.buffer = []

    # Создание файла для хранения данных, если он не существует
    def create_file(self):
        with open(self.path, "w") as _:
            pass

    # Полная запись данных из буфера в файл CSV и очистка буфера
    def write(self, separator: str):
        with open(self.path, 'a') as f:
            for element in self.buffer:
                f.write(separator.join(map(str, element)) + '\n')

    def flush(self):
        self.write(' ')
        self.buffer = []

    # Проверка размера буфера
    def check_limit(self):
        if len(self.buffer) >= self.buffer_limit:
            self.flush()

    # Добавление новой метрики в буфер
    def add_metric(self, metric_name: str, value: int):
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%z')
        self.buffer.append((timestamp, metric_name, str(value)))
        self.check_limit()


class CsvStorage(TxtStorage):
    def create_file(self):
        """
        Если файл существует, проверяется, содержит ли он заголовок.
        Если файл пустой или только что создан, записывается заголовок.
        """
        file_exists = os.path.exists(self.path)
        if not file_exists or os.stat(self.path).st_size == 0:
            header = 'date;metric;value\n'
        else:
            header = ''
        with open(self.path, 'a' if header == '' else 'w') as f:
            f.write(header)

    def flush(self):
        self.write(';')
        self.buffer = []


class Statsd:
    def __init__(self, storage: TxtStorage):
        """
        - storage: хранилище для записи метрик.
        - создаём файл для хранения метрик
        """
        self.storage = storage
        self.storage.create_file()

    # Очень нужные функции для работы с контекстным менеджером
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.storage.flush()

    # Увеличение значения метрики на 1
    def incr(self, metric_name: str):
        self.storage.add_metric(metric_name, 1)

    # Уменьшение значения метрики на 1
    def decr(self, metric_name: str):
        self.storage.add_metric(metric_name, -1)


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    if not path.endswith(".txt"):
        raise ValueError("Некорректное расширение файла. Ожидаются .txt или .csv.")
    storage = TxtStorage(path, buffer_limit)
    return Statsd(storage)


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    if not path.endswith(".csv"):
        raise ValueError("Некорректное расширение файла. Ожидаются .txt или .csv.")
    storage = CsvStorage(path, buffer_limit)
    return Statsd(storage)
