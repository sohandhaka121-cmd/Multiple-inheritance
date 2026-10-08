# Multiple Inheritance

class Creature:
    def __init__(self, c, e):
        self.color = c
        self.eat = e

    def Show_info(self):
        print(f"Color: {self.color}\nEat: {self.eat}")


class Pet:
    def __init__(self, o):
        self.owner = o

    def Show_info(self):
        print(f"Owner : {self.owner}")


class Dog(Pet, Creature):
    def __init__(self, n, c, e, o):
        Creature.__init__(self, c, e)
        Pet .__init__(self, o)
        self.name = n

    def Show_info(self):
        Creature.Show_info(self)
        Pet.Show_info(self)
        print(f"Dog name: {self.name}")

dog1 = Dog("Tommy", "Black", "meat", "Sohanur")
dog1.Show_info()
