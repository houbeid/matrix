class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def to_row_echelon_form(self):
        matrix = [row[:] for row in self.data]  # Copie de la matrice
        lead = 0

        for r in range(self.rows):
            if lead >= self.cols:
                break

            i = r
            while i < self.rows and matrix[i][lead] == 0:
                i += 1
            if i == self.rows:
                lead += 1
                if lead == self.cols:
                    break
                r -= 1  # Reste sur la même ligne
                continue

            # Échange la ligne i avec la ligne r
            matrix[i], matrix[r] = matrix[r], matrix[i]

            # Normalise la ligne r
            lv = matrix[r][lead]
            if lv != 0:
                matrix[r] = [x / lv for x in matrix[r]]

            # Élimine les éléments en dessous du pivot
            for i in range(r + 1, self.rows):
                lv = matrix[i][lead]
                matrix[i] = [
                    iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])
                ]

            lead += 1

        return Matrix(matrix)

    def display(self):
        for row in self.data:
            print(["{:.2f}".format(x) for x in row])
        print()


def main():
    # Exemple de matrice à transformer
    data = [
        [0, 0, 5, 1],
        [0, 0, 0, 0],
        [3, 6, 9, 0]
    ]

    print("Matrice initiale :")
    matrix = Matrix(data)
    matrix.display()

    ref = matrix.to_row_echelon_form()

    print("Forme échelonnée (Row-Echelon Form) :")
    ref.display()


if __name__ == "__main__":
    main()
