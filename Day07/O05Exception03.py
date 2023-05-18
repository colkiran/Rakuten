
class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

class TooTiny(Exception):
    pass


print("Checking the age to cast a vote")

try:
    age = int(input("Enter the age :"))
    if age <= 10:
        raise TooTiny("Too very young to vote......")
    elif age < 18:
        raise TooYoung("Not the right age to vote.....")
    elif age > 100:
        raise TooOld("Too old to cast a vote......")
    else:
        print("You can cast your valuable vote.......")
except TooTiny as t:
    print(t)
except TooYoung as y:
    print(y)
except TooOld as o:
    print(o)
except Exception as e:
    print(e)
finally:
    print("Completed the job of casting vote")