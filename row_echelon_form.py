class Matrix:
    def __init__(self, values):
        self.values = [row[:] for row in values]
        self.rows = len(values)
        self.cols = len(values[0]) if values else 0

    def rref(self):
        A = self.values
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
                        return
            A[r], A[i] = A[i], A[r]
            lv = A[r][lead]
            A[r] = [mrx / lv for mrx in A[r]]
            for i in range(rowCount):
                if i != r:
                    lv = A[i][lead]
                    A[i] = [iv - lv * rv for rv, iv in zip(A[r], A[i])]
            lead += 1

    def display(self):
        for row in self.values:
            print(["{:.7f}".format(val) for val in row])


def main():
    matrix = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.]
    ])
    print("Matrice originale :")
    matrix.display()

    matrix.rref()
    print("\nForme échelonnée réduite (RREF) :")
    matrix.display()


if __name__ == "__main__":
    main()
