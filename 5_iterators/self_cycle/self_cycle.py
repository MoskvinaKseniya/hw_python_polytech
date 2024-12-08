from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

''' Функция cycle() создает бесконечный итератор,
    возвращающий элементы из итерируемой последовательности iterable и сохраняющий копию каждого элемента.
    Когда последовательность iterable исчерпана, начинает возвращать элементы из сохраненной копии.
'''


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    while True:
        for item in obj:
            yield item


class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.obj = list(obj)
        self.index = None

    def __iter__(self):
        return self

    def __next__(self):
        # получается с условием на if не нужна обработка исключений StopIteration?
        if self.index is None or self.index >= len(self.obj):
            self.index = 0
        result = self.obj[self.index]
        self.index += 1
        return result
