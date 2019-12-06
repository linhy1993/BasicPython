class Fib(object):
    # iterator
    def __init__(self, n):
        self.cur = 1
        self.prev = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.n > 0:
            value = self.cur
            self.cur, self.prev = self.cur + self.prev, self.cur
            self.n -= 1
            return value
        raise StopIteration()


def fib_gen(n):
    prev, cur = 0, 1
    while n > 0:
        value = cur
        prev, cur = cur, prev + cur
        n -= 1
        yield value

if __name__ == '__main__':
    fib_iter = Fib(2)
    print([i for i in fib_iter])
    for i in fib_gen(10):
        print(i)