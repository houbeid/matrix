import math
from typing import Union, List

Number = Union[int, float]

def lerp_value(u: Number, v: Number, t: float) -> float:
    return math.fma(t, v - u, u)

def lerp_vector(u: List[Number], v: List[Number], t: float) -> List[float]:
    if len(u) != len(v):
        raise ValueError("Les vecteurs doivent avoir la même taille.")
    return [math.fma(t, v[i] - u[i], u[i]) for i in range(len(u))]

def lerp_matrix(u: List[List[Number]], v: List[List[Number]], t: float) -> List[List[float]]:
    if len(u) != len(v) or len(u[0]) != len(v[0]):
        raise ValueError("Les matrices doivent avoir la même taille.")
    return [
        [math.fma(t, v[i][j] - u[i][j], u[i][j]) for j in range(len(u[0]))]
        for i in range(len(u))
    ]


if __name__ == "__main__":
    print(lerp_value(0., 1., 0.)) 
    print(lerp_value(0., 1., 1.)) 
    print(lerp_value(0., 1., 0.5))
    print(lerp_value(21., 42., 0.3))

    u_vec = [2., 1.]
    v_vec = [4., 2.]
    print(lerp_vector(u_vec, v_vec, 0.3))

    u_mat = [[2., 1.], [3., 4.]]
    v_mat = [[20., 10.], [30., 40.]]
    result = lerp_matrix(u_mat, v_mat, 0.5)
    for row in result:
        print(row)
