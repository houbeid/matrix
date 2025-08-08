from typing import List

class Matrix:
    def __init__(self, values: List[List[float]]):
        if not values:
            raise ValueError("La matrice ne peut pas être vide.")
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0])
        
        for row in values:
            if len(row) != self.cols:
                raise ValueError("Toutes les lignes doivent avoir le même nombre de colonnes.")

    def trace(self) -> float:
        if self.rows != self.cols:
            raise ValueError("La matrice doit être carrée (autant de lignes que de colonnes).")
        result = 0.0
        for i in range(self.rows):
            result += self.values[i][i]
        return result

    def __str__(self):
        return "\n".join(str(row) for row in self.values)


def main():
    print("Exemple 1 :")
    A = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])
    print("// ", A.trace())

    B = Matrix([
        [2.0, -1.0],
        [4.5, 3.0]
    ])
    print("// ", B.trace())

    try:
        C = Matrix([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ])
        print("// ", C.trace())  # Doit lever une erreur
    except ValueError as e:
        print("Erreur :", e)

if __name__ == "__main__":
    main()
