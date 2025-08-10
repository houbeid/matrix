import math
from typing import Union, List

Number = Union[int, float]

class Vector:
    """Classe représentant un vecteur mathématique."""

    def __init__(self, values: List[Number]):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index: int):
        return self.values[index]

    def __str__(self):
        return '\n'.join([f"[{x}]" for x in self.values])

    def lerp(self, other: 'Vector', t: float) -> 'Vector':
        """Interpolation entre deux vecteurs."""
        if len(self.values) != len(other.values):
            raise ValueError("Les vecteurs doivent avoir la même taille.")
        return Vector([math.fma(t, other.values[i] - self.values[i], self.values[i])
                       for i in range(len(self.values))])

    def __repr__(self) -> str:
        return f"Vector({self.values})"


class Matrix:
    """Classe représentant une matrice composée de vecteurs."""

    def __init__(self, rows: List[Vector]):
        if not rows:
            raise ValueError("La matrice ne peut pas être vide.")
        row_length = len(rows[0].values)
        if not all(len(row.values) == row_length for row in rows):
            raise ValueError("Toutes les lignes doivent avoir la même taille.")
        self.rows = rows

    def lerp(self, other: 'Matrix', t: float) -> 'Matrix':
        """Interpolation entre deux matrices."""
        if len(self.rows) != len(other.rows):
            raise ValueError("Les matrices doivent avoir le même nombre de lignes.")
        return Matrix([self.rows[i].lerp(other.rows[i], t) for i in range(len(self.rows))])

    def __repr__(self):
        return "[" + ",\n ".join(str(row.values) for row in self.rows) + "]"


def main():
    # ---- SCALAIRE ----
    def lerp_value(u: Number, v: Number, t: float) -> float:
        return math.fma(t, v - u, u)

    print(lerp_value(0., 1., 0.))
    print(lerp_value(0., 1., 1.))
    print(lerp_value(0., 1., 0.5))
    print(lerp_value(21., 42., 0.3))

    # ---- VECTEUR ----
    u_vec = Vector([2., 1.])
    v_vec = Vector([4., 2.])
    print("// ", u_vec.lerp(v_vec, 0.3))

    # ---- MATRICE ----
    u_mat = Matrix([Vector([2., 1.]), Vector([3., 4.])])
    v_mat = Matrix([Vector([20., 10.]), Vector([30., 40.])])
    print("// ", u_mat.lerp(v_mat, 0.5))


if __name__ == "__main__":
    main()
