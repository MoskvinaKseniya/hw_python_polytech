from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

''' Функция chain() создает итератор, который возвращает элементы из первой iterables,
    пока она не будет исчерпана, а затем переходит к следующей iterables,
    пока все итерируемые последовательности не будут исчерпаны.
'''


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    for iterable in iterables:
        for item in iterable:
            yield item


class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.iterables = iterables
        self.iterable = iter(iterables[0])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> T:
        try:
            return next(self.iterable)
        # переход к следующему объекту
        except StopIteration:
            self.index += 1
            if self.index < len(self.iterables):
                self.iterable = iter(self.iterables[self.index])
                return next(self.iterable)
            else:
                raise StopIteration
