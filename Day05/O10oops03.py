
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 33
        print("Player Initialized.....")

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")


ply1 = Player()
ply1.get_details()

print("-" * 40)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 30
ply2.get_details()


