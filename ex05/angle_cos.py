import math
from typing import List

class Vector:
    def __init__(self, values: List[float]):
        self.data = list(values)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index: int):
        return self.data[index]

    def __str__(self):
        return '\n'.join([f"[{x}]" for x in self.data])

    def norm_2(self) -> float:
        sum_sq = 0.0
        for x in self.data:
            sum_sq = math.fma(x, x, sum_sq)
        return self.sqrt(sum_sq)

    # Racine carrée sans sqrt ni pow
    def sqrt(self, x: float, iterations: int = 10) -> float:
        if x == 0.0:
            return 0.0
        guess = x
        for _ in range(iterations):
            guess = 0.5 * (guess + x / guess)
        return guess

def dot_product(u: Vector, v: Vector) -> float:
    if len(v) != len(u):
        raise ValueError("Les vecteurs doivent être de même taille.")
    result = 0.0
    for a, b in zip(u, v):
        result = math.fma(a, b, result)
    return result

def angle_cos(u: Vector, v: Vector) -> float:
    if len(u) != len(v):
        raise ValueError("Les vecteurs doivent être de même taille.")

    norm_u = u.norm_2()
    norm_v = v.norm_2()

    if norm_u == 0.0 or norm_v == 0.0:
        raise ValueError("Le cosinus est indéfini pour un vecteur nul.")

    return dot_product(u, v) / (norm_u * norm_v)

if __name__ == "__main__":
    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    print("// ", angle_cos(u, v))
