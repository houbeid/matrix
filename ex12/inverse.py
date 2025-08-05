class Matrix:
    def __init__(self, data):
        self.data = data
        self.n = len(data)

    @classmethod
    def from_list(cls, data):
        return cls(data)

    def is_square(self):
        return all(len(row) == self.n for row in self.data)

    def identity(self):
        return [[1.0 if i == j else 0.0 for j in range(self.n)] for i in range(self.n)]

    def inverse(self):
        if not self.is_square():
            raise ValueError("Matrix is not square.")

        n = self.n
        mat = [row[:] for row in self.data]
        inv = self.identity()

        for i in range(n):
            pivot = mat[i][i]
            if pivot == 0:
                # Try to swap with a row below
                for j in range(i+1, n):
                    if mat[j][i] != 0:
                        mat[i], mat[j] = mat[j], mat[i]
                        inv[i], inv[j] = inv[j], inv[i]
                        pivot = mat[i][i]
                        break
                else:
                    raise ValueError("Matrix is singular and cannot be inverted.")

            # Normalize the pivot row
            for j in range(n):
                mat[i][j] /= pivot
                inv[i][j] /= pivot

            # Eliminate other rows
            for k in range(n):
                if k != i:
                    factor = mat[k][i]
                    for j in range(n):
                        mat[k][j] -= factor * mat[i][j]
                        inv[k][j] -= factor * inv[i][j]

        return Matrix(inv)

    def __str__(self):
        return '\n'.join(['[' + ', '.join(f"{val:.9f}" for val in row) + ']' for row in self.data])


# === Main function for testing ===
def main():
    matrices = [
        ([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]], "Identity"),
        ([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]], "Diagonal"),
        ([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]], "General")
    ]

    for mat_data, label in matrices:
        print(f"\n=== {label} Matrix ===")
        u = Matrix.from_list(mat_data)
        try:
            inv = u.inverse()
            print("Inverse:")
            print(inv)
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
