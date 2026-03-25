class Person:
    def __init__(self, name, parent1, parent2):
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2
        

class FamilyTree:
    def __init__(self):
        self.head = None

    def create(self, name, parent1, parent2, file):
        with open(file, "w") as file:
            person = Person(name, parent1, parent2)
            file.write(f"{person.name}, {person.parent1}, {person.parent2}\n")

    def read(self, file):
        pass

        
file = "bleh.csv"
ft = FamilyTree()
ft.create("Alaya", 1, 2, file)
    