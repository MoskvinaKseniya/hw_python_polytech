from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

''' Функция batched() разбивает пакетные данные из итерируемого объекта iterable на кортежи длиной n.
    Последняя партия может быть короче n.
'''


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""
    batch = []
    for item in obj:
        batch.append(item)
        if len(batch) == n:
            yield tuple(batch)
            batch = []
    # если остался неполный батч
    if batch:
        yield tuple(batch)


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        """Реализуй этот класс."""
        self.obj = iter(obj)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self) -> tuple[T, ...]:
        batch = []
        for item in range(self.n):
            try:
                batch.append(next(self.obj))
            except StopIteration:
                if batch:
                    return tuple(batch)
                else:
                    raise StopIteration
        return tuple(batch)
