import math
from typing import Union, List

Number = Union[int, float]

def lerp_value(u: Number, v: Number, t: float) -> float:
    """Interpolation linéaire entre deux scalaires"""
    return math.fma(t, v - u, u)

def lerp_vector(u: List[Number], v: List[Number], t: float) -> List[float]:
    """Interpolation linéaire entre deux vecteurs"""
    if len(u) != len(v):
        raise ValueError("Les vecteurs doivent avoir la même taille.")
    return [math.fma(t, v[i] - u[i], u[i]) for i in range(len(u))]

def lerp_matrix(u: List[List[Number]], v: List[List[Number]], t: float) -> List[List[float]]:
    """Interpolation linéaire entre deux matrices"""
    if len(u) != len(v) or len(u[0]) != len(v[0]):
        raise ValueError("Les matrices doivent avoir la même taille.")
    return [
        [math.fma(t, v[i][j] - u[i][j], u[i][j]) for j in range(len(u[0]))]
        for i in range(len(u))
    ]

# ======= MAIN =======
if __name__ == "__main__":
    # Cas scalaire
    print(lerp_value(0., 1., 0.))   # 0.0
    print(lerp_value(0., 1., 1.))   # 1.0
    print(lerp_value(0., 1., 0.5))  # 0.5
    print(lerp_value(21., 42., 0.3)) # 27.3

    # Cas vecteur
    u_vec = [2., 1.]
    v_vec = [4., 2.]
    print(lerp_vector(u_vec, v_vec, 0.3)) # [2.6, 1.3]

    # Cas matrice
    u_mat = [[2., 1.], [3., 4.]]
    v_mat = [[20., 10.], [30., 40.]]
    result = lerp_matrix(u_mat, v_mat, 0.5)
    for row in result:
        print(row)
    # Résultat attendu :
    # [11.0, 5.5]
    # [16.5, 22.0]
