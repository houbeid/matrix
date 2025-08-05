from typing import List

class Matrix:
    def __init__(self, values: List[List[float]]):
        if not values or not values[0]:
            raise ValueError("La matrice ne peut pas être vide.")
        
        row_length = len(values[0])
        for row in values:
            if len(row) != row_length:
                raise ValueError("Toutes les lignes doivent avoir le même nombre de colonnes.")

        self.values = values
        self.rows = len(values)
        self.cols = row_length

    def transpose(self) -> 'Matrix':
        transposed = [
            [self.values[i][j] for i in range(self.rows)]
            for j in range(self.cols)
        ]
        return Matrix(transposed)

    def display(self):
        for row in self.values:
            print(" ".join(f"{val:.2f}" for val in row))


def main():
    A = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ])

    print("Matrice originale :")
    A.display()

    B = A.transpose()
    print("\nMatrice transposée :")
    B.display()


if __name__ == "__main__":
    main()
