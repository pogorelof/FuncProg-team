def show(matrix):
    for i in matrix:
        print(*i)
    print()


def matrix_operations(m1, m2, op):
    result = [[0,0,0], 
              [0,0,0], 
              [0,0,0]] 
    if op == '+':
        for i in range(len(m1)): 
            for j in range(len(m1[0])): 
                result[i][j] = m1[i][j] + m2[i][j] 
    if op == '-':
        for i in range(len(m1)): 
            for j in range(len(m1[0])): 
                result[i][j] = m1[i][j] - m2[i][j] 
    if op == '*':
        for i in range(len(m1)):
            for j in range(len(m1)):
                for k in range(len(m1)):
                    result[i][j] += m1[i][k] * m2[k][j]
    return result

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

print('Матрица 1:')
show(matrix1)
print('Матрица 2:')
show(matrix2)

print('Сложение:')
show(matrix_operations(matrix1, matrix2, '+'))
print('Вычитание:')
show(matrix_operations(matrix1, matrix2, '-'))
print('Умножение:')
show(matrix_operations(matrix1, matrix2, '*'))