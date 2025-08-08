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

    @staticmethod
    def _abs_no_builtin(x: float) -> float:
        return x if x >= 0 else -x

    def norm_1(self) -> float:
        result = 0.0
        for i in range(len(self)):
            result = math.fma(1.0, self._abs_no_builtin(self[i]), result)
        return result

    def norm_2(self) -> float:
        result = 0.0
        for i in range(len(self)):
            squared = math.pow(self[i], 2)
            result = math.fma(1.0, squared, result)
        return math.pow(result, 0.5)

    def norm_inf(self) -> float:
        max_val = 0.0
        for i in range(len(self)):
            val = self._abs_no_builtin(self[i])
            max_val = max(max_val, val)
        return max_val

def main():
    v = Vector([3.0, -4.0, 2.0])
    print("// ", v.norm_1())
    print("// ", v.norm_2())
    print("// ", v.norm_inf())

if __name__ == "__main__":
    main()

