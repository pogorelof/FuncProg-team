def show(matrix):
    for i in matrix:
        print(*i)

def rotate(matrix):
    rotated = tuple(zip(*matrix[::-1]))
    return rotated

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

show(matrix)
matrix = rotate(matrix)
print()
show(matrix)