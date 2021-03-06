'''Дано нечетное число n. Создайте двумерный массив из n×n элементов,
заполнив его символами "." (каждый элемент массива является строкой из одного символа).
Затем заполните символами "*" среднюю строку массива, средний столбец массива,
главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать
изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.'''

n = int(input('Input odd numeric : '))

canvas = [['.' for j in range(n)] for i in range(n)]
for i in range(n):
    canvas[i][i] = '*'
    canvas[i][n - 1 - i] = '*'
    canvas[(n-1)//2][i] = '*'
    canvas[i][(n-1)//2] = '*'

for line in canvas:
    print(' '.join(line))
