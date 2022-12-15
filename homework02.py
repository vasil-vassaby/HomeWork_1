# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f'Для значений x = {x}, y= {y}, z = {z}: ')
                print(f'утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> {not (x or y or z) == (not x and not y and not z)}')

