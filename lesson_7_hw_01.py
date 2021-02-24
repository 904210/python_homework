class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(matrix)


matrix_one = Matrix([[4, 5, 6], [7, 8, 9], [1, 2, 3]])
matrix_two = Matrix([[2, 4, 3], [6, 3, 2], [5, 1, 4]])
print(matrix_one)
print()
print(matrix_two)
print()
print(matrix_one + matrix_two)
