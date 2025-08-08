class Matrix:
    def __init__(self, values):
        self.values = [row[:] for row in values]
        self.rows = len(values)
        self.cols = len(values[0]) if values else 0

    @classmethod
    def from_list(cls, data):
        return cls(data)

    def row_echelon(self):
        A = [row[:] for row in self.values]  # copie
        lead = 0
        rowCount = self.rows
        columnCount = self.cols

        for r in range(rowCount):
            if lead >= columnCount:
                break
            i = r
            while abs(A[i][lead]) < 1e-9:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return Matrix(A)
            A[r], A[i] = A[i], A[r]
            lv = A[r][lead]
            A[r] = [mrx / lv for mrx in A[r]]
            for i in range(rowCount):
                if i != r:
                    lv = A[i][lead]
                    A[i] = [iv - lv * rv for rv, iv in zip(A[r], A[i])]
            lead += 1
        return Matrix(A)

    def rank(self):
        ref = self.row_echelon().values
        rank_count = 0
        for row in ref:
            if any(abs(val) > 1e-12 for val in row):
                rank_count += 1
        return rank_count

    def __str__(self):
        return '\n'.join(
            ['[' + ', '.join(f"{val:.7f}" for val in row) + ']' for row in self.values]
        )


def main():
    matrices = [
        ([[1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 1.]], "Identité"),

        ([[1., 2., 0., 0.],
          [2., 4., 0., 0.],
          [-1., 2., 1., 1.]], "Dépendance linéaire"),

        ([[8., 5., -2.],
          [4., 7., 20.],
          [7., 6., 1.],
          [21., 18., 7.]], "4x3 exemple")
    ]

    for mat_data, label in matrices:
        u = Matrix.from_list(mat_data)
        print("// ", u.rank())


if __name__ == "__main__":
    main()
