class Vector:
    def __init__(self, data):
        self.data = list(data)
    def add (self, other):
        if len(self.data) != len(other.data):
            raise ValueError("taille different")
        self.data = [a + b for a , b in zip(self.data, other.data)]
        