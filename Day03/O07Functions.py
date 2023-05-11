
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# gname is non default argument, city is default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")


greet()

print("-" * 40)
greetGst("Sachin")
greetGst("Rahul")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

# variable length arguments
print("-" * 40)
# *var can accept more than one value in the form of a list

def prodAll(*numbers):
    print(f"numbers :{numbers}")
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(f"The product of 1, 2, 3, 4 and 5 is :{prodAll(1, 2, 3, 4, 5)}")

print("-" * 40)
# **var - accepts data like a dictionary
def extract_details(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)


extract_details(name="Rahul", age=29, runs=150, oppn='West Indies')
