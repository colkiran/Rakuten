
"""
client - name should be accepted as first name and last name
"""

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Ctor.......")

    def get_detials(self):
        print(f"Name is {self.name} and Age is {self.age} ")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("factory.......")
        plyr = cls(f"{fn} {ln}", age)
        return plyr

ply1 = Player("Virat Kholi", 30)
ply1.get_detials()

print("-" * 40)
ply2 = Player.CreatePlayer("Rohit", "Sharma", 29)
ply2.get_detials()
