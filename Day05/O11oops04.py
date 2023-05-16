
class Player:

    def __init__(self, name, age):
        self.name= name
        self.age  = age
        print("Player Initialized........")

    def get_detials(self):
        print(f"Name is {self.name} and Age is {self.age} ")

ply1 = Player("Sachin", 32)
ply1.get_detials()

print("-" * 40)

ply2 = Player("Sourav", 30)
ply2.get_detials()

print("-" * 40)

print(ply1.__dict__)
print(ply2.__dict__)

ply2.runs = 125
print(ply2.__dict__)
print(ply1.__dict__)


"""
self will have the name of the object that made a call to the method

class A:
    def __init__(self, name, age):
        self.name = name
        
    def fun(self):          # self will a stored in it
        print("hello world")
        print(self.name)
        
a = A("jack")
a.fun()

----------------------
b = A("jill")
b.fun()

"""