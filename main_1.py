from decimal import Decimal

first_value = 0.1 + 0.2 + 0.3 - 0.5
print(first_value)
second_value = Decimal('0.1')+Decimal('0.2')+Decimal('0.3')-Decimal('0.5')
print(second_value)
number_one = 1.37
number_two = 5.5
print(Decimal.from_float(number_one))
print(Decimal(str(number_one)))
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
