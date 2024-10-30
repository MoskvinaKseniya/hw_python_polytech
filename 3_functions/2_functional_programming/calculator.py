# Функции для чисел
def zero(function=None):
    return 0 if function is None else function(0)


def one(action=None):
    return 1 if action is None else action(1)


def two(action=None):
    return 2 if action is None else action(2)


def three(action=None):
    return 3 if action is None else action(3)


def four(action=None):
    return 4 if action is None else action(4)


def five(action=None):
    return 5 if action is None else action(5)


def six(action=None):
    return 6 if action is None else action(6)


def seven(action=None):
    return 7 if action is None else action(7)


def eight(action=None):
    return 8 if action is None else action(8)


def nine(action=None):
    return 9 if action is None else action(9)


# Функции для операций
def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y
