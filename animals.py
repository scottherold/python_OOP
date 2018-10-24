class Animal:
    def __init__(self):
        self.name = "Animal"
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(self.health)
        return self.health

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dog"
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dragon"
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print("I am a Dragon")        

animal1 = Animal()
animal1.walk().walk().walk().run().run().displayHealth()

animal2 = Dog()
animal2.walk().walk().walk().run().run().pet().displayHealth()

animal3 = Dragon()
animal3.walk().walk().walk().run().run().fly().displayHealth()