# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите число: '))

if number == 6 or number == 7:
    print('Является ли этот день выходным: да')
elif number <= 0 or number >= 8:
    print('ошибка, введите значение от 1 до 7!')
else:
    print('Является ли этот день выходным: нет')