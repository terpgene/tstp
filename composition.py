class Dog():
    def __init__(self, 
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    

class Person:
    def __init__(self, name):
        self.name = name


gene = Person("Gene Essel")

hawkk = Dog("Hawkky", "Yorkie", gene)

print(hawkk.owner.name)
    