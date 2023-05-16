
class Player:       # pascal casing

    def get_runs(self):
        print("Runs scored......")

sachin = Player()           # calls the constructor (calls default Ctor)
sachin.get_runs()
print(type(sachin))

print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
