class Matrix:
    def __init__(self, data):
        if not data or not all(len(row) == len(data) for row in data):
            raise ValueError("La matrice doit être carrée.")
        self.data = data
        self.n = len(data)

    def determinant(self):
        return self._determinant_recursive(self.data)

    def _determinant_recursive(self, mat):
        n = len(mat)
        if n == 1:
            return mat[0][0]
        if n == 2:
            return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

        det = 0
        for col in range(n):
            minor = [row[:col] + row[col+1:] for row in mat[1:]]
            cofactor = ((-1) ** col) * mat[0][col] * self._determinant_recursive(minor)
            det += cofactor
        return det

    @classmethod
    def from_list(cls, rows):
        return cls(rows)

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)
def main():
    u = Matrix.from_list([
        [1., -1.],
        [-1., 1.],
    ])
    print("// ", u.determinant())

    u = Matrix.from_list([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    print("// ", u.determinant())

    u = Matrix.from_list([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print("// ", u.determinant())

    u = Matrix.from_list([
        [8., 5., -2., 4.],
        [4., 2.5, 20., 4.],
        [8., 5., 1., 4.],
        [28., -4., 17., 1.],
    ])
    print("// ", u.determinant())


if __name__ == "__main__":
    main()
