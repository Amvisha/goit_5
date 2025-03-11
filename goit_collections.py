import collections

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)
print(person.post_index)
print(person.age)
print(person[3])

student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5, 6, 6]
mark_counts = collections.Counter(student_marks)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

mark_counts = collections.Counter(student_marks)
print(mark_counts)

# Створення Counter з рядка
letter_count = collections.Counter("banana")
print(letter_count)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = collections.Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")

# Створення defaultdict з list як фабрикою за замовчуванням
d = collections.defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = collections.defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)


from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))


from collections import Counter

def num_counter(filename, n):
    with open(filename, 'r') as file:
        data = file.read()
    data_updated = [int(i) for i in data.split(',')]
    counter = Counter(data_updated)
    print(counter)
    order = counter.most_common(len(counter))
    return order[:n], order[-n:]

most, least = num_counter('numbers.txt', 5)
print(f"Most {most} \nLeast {least}")

from collections import namedtuple

cat_info = namedtuple('Cat', ['nickname', 'age', 'owner'])
bobs_cat = cat_info('Alex', 2, 'Bob')

print(bobs_cat)
print(bobs_cat.nickname)

from collections import namedtuple

rgb = namedtuple('RGB', ['red', 'green', 'blue'])
black = rgb(0, 0, 0)
indigo = rgb(0, 65, 106)
ocean_wave = rgb(143, 201, 184)


print(ocean_wave.red, indigo.blue)
print(indigo.green - ocean_wave.green)


from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636', '0509993637', '0639993636', '0509993632', '0339993632']

phone_operators_number = defaultdict(list)

for phone in phone_numbers:
    if phone.startswith('050') or phone.startswith('095'):
        phone_operators_number['Vodafone'].append(phone)
    elif phone.startswith('067') or phone.startswith('096'):
        phone_operators_number['Kyivstar'].append(phone)
    elif phone.startswith('063') or phone.startswith('093'):
        phone_operators_number['Lifecell'].append(phone)
    else:
        phone_operators_number['Other_operators'].append(phone)

print(phone_operators_number)
print(phone_operators_number.get('Kyivstar'))
print(phone_operators_number.get('Kyivstars'))
print(phone_operators_number)