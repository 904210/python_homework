class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        matrix = [[0 * el for el in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(matrix)


matrix_one = Matrix([[4, 5, 6, 5], [7, 8, 9, 2], [1, 2, 3, 1]])
matrix_two = Matrix([[2, 4, 3, 2], [6, 3, 2, 2], [5, 1, 4, 2]])
print(matrix_one)
print()
print(matrix_two)
print()
print(matrix_one + matrix_two)
