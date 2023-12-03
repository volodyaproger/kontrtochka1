def restore_matrix(arr):
    n = int((len(arr) * 2) ** 0.5)
    matrix = [[0] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = matrix[j][i] = arr[index]
            index += 1

    return matrix


def write_matrix_to_file(matrix, filename):
    with open("Канакин_У-234_vivod.txt", 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')


def read_matrix_from_file(filename):
    matrix = []
    with open("Канакин_У-234_vvod.txt", 'r') as file:
        for line in file:
            row = list(map(str, line.split()))
            matrix.append(row)
    return matrix


input_file = "Канакин_У-234_vvod.txt"
output_file = "Канакин_У-234_vivod.txt"

arr = read_matrix_from_file(input_file)
matrix = restore_matrix(arr)
write_matrix_to_file(matrix, output_file)
