matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
diag = [matrix[i][i] for i in range(len(matrix))]
trace = sum(diag)
znach = trace / len(matrix)

for i in range(len(matrix)): 
    if i % 2 == 0:
        matrix[i] = [x / znach for x in matrix[i]]

print("Диагональные элементы:", diag)
print("След матрицы:", trace) 
print("Преобразованная матрица:") 
for row in matrix: 
    print(row)
