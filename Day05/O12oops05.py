"""
class attribute can be accessed only by class name

"""
class Player:

    team = "India"      # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_detials(self):
        print(f"Name is {self.name} and Age is {self.age} ")

ply1 = Player("Sachin", 32)
ply1.get_detials()

print("-" * 40)
ply2 = Player("Rahul", 33)
ply2.get_detials()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
Player.team = "Mumbai Indians"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
ply2.team = "Rajasthan Royals"          # will not update the class attribute
print(f"ply2   :{ply2.team}")
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")
