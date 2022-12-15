# Напишите программу, которая
# принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Введите координаты точки: ")
x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print('Указанные координаты соответствуют четверти -> 1')
elif x < 0 and y > 0:
    print('Указанные координаты соответствуют четверти -> 2')
elif x < 0 and y < 0:
    print('Указанные координаты соответствуют четверти -> 3')
elif x > 0 and y < 0:
    print('Указанные координаты соответствуют четверти -> 4')
elif x == 0 and (y < 0 or y > 0):
    print('Указанные координаты соответствуют оси -> y')
elif y == 0 and (x < 0 or x > 0):
    print('Указанные координаты соответствуют оси -> x')
else:
    print('Введены некорректные координаты')
