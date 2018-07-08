class Square:
    pass

print(Square)

class Lion:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

lion = Lion("Genetic")
print(lion)