from typing import List, Union

class Matrix:
    def __init__(self, values: List[List[float]]):
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0]) if values else 0

    def mul_vec(self, vector: List[float]) -> List[float]:
        if self.cols != len(vector):
            raise ValueError("Nombre de colonnes de la matrice doit correspondre à la taille du vecteur.")
        result = []
        for row in self.values:
            result.append(sum(a * b for a, b in zip(row, vector)))
        return result

    def mul_mat(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError("Nombre de colonnes de la 1ère matrice doit correspondre au nombre de lignes de la 2e matrice.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.values[i][k] * other.values[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.values)
u = Matrix([
    [1., 0.],
    [0., 1.]
])
v = [4., 2.]
print(u.mul_vec(v))


u = Matrix([
    [2., 0.],
    [0., 2.]
])
v = [4., 2.]
print(u.mul_vec(v))

u = Matrix([
    [2., -2.],
    [-2., 2.]
])
v = [4., 2.]
print(u.mul_vec(v))

u = Matrix([
    [1., 0.],
    [0., 1.]
])
v = Matrix([
    [1., 0.],
    [0., 1.]
])
print(u.mul_mat(v))

u = Matrix([
    [1., 0.],
    [0., 1.]
])
v = Matrix([
    [2., 1.],
    [4., 2.]
])
print(u.mul_mat(v)) 


u = Matrix([
    [3., -5.],
    [6., 8.]
])
v = Matrix([
    [2., 1.],
    [4., 2.]
])
print(u.mul_mat(v))
