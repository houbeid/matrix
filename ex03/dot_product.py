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
    
def dot_product(u: Vector, v: Vector) -> float:
    if len(v) != len(u):
        raise ValueError("Les vecteurs doivent être de même taille.")
    result = 0
    for a, b in zip(u, v):
        result = math.fma(a, b, result)
    return result
if __name__ == "__main__":
    u = Vector([1.0, 3.0, -5.0])
    v = Vector([4.0, -2.0, -1.0])
    print("// ", dot_product(u, v))