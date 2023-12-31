"""
Дан двумерный массив и два числа: i и j. Поменяйте в
массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем
элементы массива, затем числа i и j.
"""

n, m = map(int, input("Введите размеры массива (через пробел): ").split())

matrix = []
for _ in range(n):
    row = list(map(int, input("Введите элементы строки массива (через пробел): ").split()))
    matrix.append(row)

i, j = map(int, input("Введите числа i и j (через пробел): ").split())

# Проверяем введенные значения i и j на корректность
if i < 0 or i >= m or j < 0 or j >= m:
    print("Некорректные значения i и j")
else:
    # Меняем столбцы i и j местами
    for k in range(n):
        matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

    # Выводим результат
    print("Результат:")
    for row in matrix:
        print(*row)
