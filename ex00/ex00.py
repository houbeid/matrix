class Vector:
    def __init__(self, data):
        self.data = list(data)
    
    def add(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Les vecteurs doivent être de même taille.")
        self.data = [a + b for a, b in zip(self.data, other.data)]
    
    def sub(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Les vecteurs doivent être de même taille.")
        self.data = [a - b for a, b in zip(self.data, other.data)]
    
    def scl(self, scalar):
        self.data = [a * scalar for a in self.data]
    
    def __str__(self):
        return '\n'.join(f"[{x}]" for x in self.data)

class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]
    
    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Les matrices doivent être de même taille.")
        self.data = [
            [a + b for a, b in zip(row_self, row_other)]
            for row_self, row_other in zip(self.data, other.data)
        ]
    
    def sub(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Les matrices doivent être de même taille.")
        self.data = [
            [a - b for a, b in zip(row_self, row_other)]
            for row_self, row_other in zip(self.data, other.data)
        ]
    
    def scl(self, scalar):
        self.data = [
            [a * scalar for a in row]
            for row in self.data
        ]
    
    def __str__(self):
        return '\n'.join(str(row) for row in self.data)
def main():
    print("=== Vecteurs ===")
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.add(v)
    print("// ", u) 

    # u = Vector([2.0, 3.0])
    # v = Vector([5.0, 7.0])
    # u.sub(v)
    # print("// ", u) 

    # u = Vector([2.0, 3.0])
    # u.scl(2.0)
    # print("// ", u) 

    print("\n=== Matrices ===")
    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    u.add(v)
    print(u) 

    # u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    # v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    # u.sub(v)
    # print(u) 

    # u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    # u.scl(2.0)
    
    # print(u)

        

if __name__ == "__main__":
    main()