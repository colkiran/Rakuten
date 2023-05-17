
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("Animal eat.....")

# inheritance

class Bird(Animal):

    def fly(self):
        print("Bird fly......")

class Fish(Animal):

    def swim(self):
        print("Fishes swim.....")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print("-" * 40)
dolphin = Fish()
dolphin.swim()
dolphin.eat()

print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)