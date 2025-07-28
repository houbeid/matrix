from typing import List

class Vector:
    def __init__(self, values: List[float]):
        if len(values) != 3:
            raise ValueError("Le vecteur doit être en dimension 3.")
        self.values = values

    def __repr__(self):
        return '\n'.join([f"[{v}]" for v in self.values])

    def __getitem__(self, index: int):
        return self.values[index]

    def __len__(self):
        return len(self.values)


def cross_product(u: Vector, v: Vector) -> Vector:
    if len(u) != 3 or len(v) != 3:
        raise ValueError("Les deux vecteurs doivent être de dimension 3.")
    
    x = u[1] * v[2] - u[2] * v[1]
    y = u[2] * v[0] - u[0] * v[2]
    z = u[0] * v[1] - u[1] * v[0]
    
    return Vector([x, y, z])


# 🔹 Exemples
u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(cross_product(u, v))
