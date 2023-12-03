a = int(input("Размер матрицы: "))
k = (a * a - a) // 2 + a
print(f'Введите {k} элементов матрицы: ')
m = []
for i in range(a):
    m.append([0] * a)
    for j in range(i, a):
        m[i][j] = int(input('-> '))

for i in range(a):
    for j in range(i, a):
        m[j][i] = m[i][j]
for row in m:
    print(row, sep='\t')
