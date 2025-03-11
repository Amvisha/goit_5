'''
def outer(x):
    def inner(y):
        print(f'{x} + {y} = {x + y}')
    return inner

def main():
    adder_two = outer(2)
    adder_two(8)
    adder_tree = outer(3)
    adder_tree(8)
'''

def get_cache(cache=None):
    if cache is None:
        cache = {}
    def inner(n):
        print(cache)
        if n not  in cache:
            cache[n] = sum([i for i in range(1, n+1)])
            print(f'Hard work: {n}')
            return cache[n]
        else:
            print(f'Easy work: {n}')
            return cache[n]
    return inner

"""def main():
    data = {5: 15, 10: 55, 15: 120}
    calc = get_cache(data)
    print(calc(5))
    print(calc(5))
    print(calc(10))
    print(calc(10))
    print(calc(15))
    print(calc(5))
"""

def factorial(n, cache={}):
    if n < 0:
        raise ValueError

    def counter(n):
        result = 1
        for value in range(1, n+1):
            if value in cache:
                result = cache[value]
            else:
                result = value * cache.get(value-1, 1)
                cache[value] = result
                print('{} not in cache {}'.format(value, result))
        return result

    return counter(n)

print(factorial(3))
print(factorial(6))
print(factorial(4))

"""if __name__ == '__main__':
    main()"""