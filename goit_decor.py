def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))


from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)

# Лямбда-функції, відомі також як анонімні функції, які є важливою частиною Python і використовуються для створення маленьких, однорядкових функцій
print((lambda x, y: x + y)(5, 3))  # Виведе 8
nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)

# Функція map() є функцією вищого порядку, що означає, що вона приймає іншу функцію як аргумент.
# map() використовується для застосування заданої функції до кожного елемента об'єкта ітерації, наприклад списку, та повертає ітератор, який виробляє результати.
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)

numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))
# Замість використання функції map():
numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)
# Ми використаємо list comprehensions:

nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

print(list(even_nums))


def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums))

def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums))

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join([x for x in some_str if x.islower()])
print(new_str)


nums = [0, False, 5, 0]
result = any(nums)
print(result)


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)
print(result)

nums = [1, 2, 3, 4]
result = all(nums)
print(result)

nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums)
print(is_all_even)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
