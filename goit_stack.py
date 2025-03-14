# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")

stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print(peek(stack))  # Виведе 'c'
print(pop(stack))  # Виведе 'c'
print(peek(stack))
print(pop(stack))
print(peek(stack))
print(pop(stack))
print(peek(stack))
print(pop(stack))

"""queue - діє за принципом "першим прийшов – першим вийшов" (FIFO: First In, First Out
Enqueue - додавання елемента в кінець черги.
Dequeue - видалення елемента з початку черги.
Front/Peek - перегляд першого елемента черги без його видалення.
Is Empty - перевірка, чи черга порожня.
Size - визначення кількості елементів у черзі."""
from collections import deque

# Створення черги
queue = deque()

# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')

print("Черга після додавання елементів:", list(queue))

# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue))

# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0])

# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0)

# Size: Розмір черги
print("Розмір черги:", len(queue))
"""Основні методи deque
append(x) - додає елемент x в кінець черги.
appendleft(x) - додає елемент x на початок черги.
pop() - видаляє та повертає елемент з правого кінця черги. Якщо черга порожня, викидає виняток IndexError.
popleft() - видаляє та повертає елемент з лівого кінця черги. Якщо черга порожня, викидає виняток IndexError."""
from collections import deque

# Створення пустої двосторонньої черги
d = deque()

# Додаємо елементи в чергу
d.append('middle')  # Додаємо 'middle' в кінець черги
d.append('last')    # Додаємо 'last' в кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги

# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))

# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())

# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())

# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)

# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

# Ініціалізація черги завдань
task_queue = deque()

# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")

# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")
