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


def linear_combination(vectors: List[Vector], scalars: List[float]) -> Vector:
    if len(vectors) != len(scalars):
        raise ValueError("Le nombre de vecteurs et de scalaires doit être identique.")
    
    dim = len(vectors[0])
    result = [0.0 for _ in range(dim)]

    for v, λ in zip(vectors, scalars):
        for i in range(dim):
            result[i] = math.fma(λ, v[i], result[i]) 
    return Vector(result)



def main():
    print("=== Test Combinaison Linéaire avec FMA ===")
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])

    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    result1 = linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
    print("// ")
    print(result1)

    result2 = linear_combination([v1, v2], [10.0, -2.0])
    print("// ")
    print(result2)


if __name__ == "__main__":
    main()
