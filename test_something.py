from faker import Faker
fake = Faker(['ru_RU', 'en_US'])
#Простые тестовые примеры

def test_sum():
    a = 5
    b = 10
    assert a == b

#Числа в двоичной системе
a = 0b010101010

#Числа в восьмиричной системе
a = 0o01234567

#Числа в шестнадцатиричной системе
a = 0x0123456789abcdef

name = str(input())
case = int(input())

number = case // 100
bed = case // 10 % 10
child = case % 10

print(f'Группа №{number}.')
print(f'{child}. {name}.')
print(f'Шкафчик: {case}.')
print(f'Кроватка: {bed}.')