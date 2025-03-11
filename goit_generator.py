squares_comp = (i**2 for i in range(11))
print(squares_comp)

# for i in squares_comp:
#     print(i)

for _ in range(10):
    print(next(squares_comp))

next(squares_comp) # StopIteration


def eight_bit_counter():
    value = 0
    while True:
        yield value
        value += 1

my_generator = eight_bit_counter()
for _ in range(6):
    print(next(my_generator))


def first_second_counter():
    while True:
        yield 1
        yield 2

my_generator = first_second_counter()
for _ in range(6):
    print(next(my_generator))


def limited_generator(limit):
    value = 0
    while value < limit:
        yield value
        value += 1

for i in limited_generator(6):
    print(i)