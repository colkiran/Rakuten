
def makepositive(func):
    def wrapper(x, y):
        if x < y:
            x, y = y, x
        print(func(x, y))

    return wrapper


@makepositive
def sub(a, b):
    return a - b


sub(10, 5)
sub(5, 10)
sub(8, 20)
