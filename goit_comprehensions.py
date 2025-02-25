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