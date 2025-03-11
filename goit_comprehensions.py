# List comprehensions використовуються для створення нових списків
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)
# Set comprehensions використовуються для створення множин
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)
# Dictionary comprehensions використовуються для створення нових словників
sq = {x: x**2 for x in range(1, 10)}
print(sq)

sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)

def get_numbers (x):
    numbers_2 = []
    for i in range(x):
        num = i ** 2
        if not num % 2:
            numbers_2.append(num)
    print(numbers_2)

def get_numbers_short(x):
    numbers_2 = {f' {i}^2' : i**2 for i in range(x) if not i % 2}
    print(numbers_2, type(numbers_2))
get_numbers(20)
get_numbers_short(20)

