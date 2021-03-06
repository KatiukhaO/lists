""" Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих
к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

n = int(input('Input size square, n : '))


matrix = [[abs(j - i) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


"""Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

m = int(input('Input m - size matrix m x m : '))

a = []
for i in range(m):
    a.append([0]*m)
    for j in range(m - i, m):
        a[i][j] = 2
        a[i][m - 1 - i] = 1
    print(' '.join(map(str, a[i])), end=' ')
    print()



