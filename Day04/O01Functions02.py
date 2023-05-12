
def Multiplyme(x, y):
    print("hello world")
    return x * y


print(Multiplyme(10, 20))

# recursive calls

# def fun(x):
#     if x <= 0:
#         exit()
#     else:
#         print(x)
#         x -= 1
#         fun(x)
#
# fun(10)

"""
using recursive calls
   1. find the factorial of a number
   2. find the fibanocci series
"""

def fact(a):
    if(a==1 or a == 0):
        return 1
    else:
        return a * fact(a-1)

z=int(input("Enter a number :"))
print(f"The factorial of {z} is :{fact(z)}")

print("=" * 40)
def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x-1) + fib(x-2)

num = int(input("Enter a number to find its Fibanocci Series :"))

for i in range(0, num + 1):
    print(fib(i), end= " ")
print()

print("-" * 40)
def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return  sum, diff, prod, quot

res = ArithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 40)
#doc strings

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)          # docstring

print("-" * 40)
def fun1(x, y):
    """
    function fun(x, y)
    ------------------

    function fun takes two arguments
    a. if the data type of the two variables are text then it gets concatenated
    b. if the data type of the two variables are numbers the it gets added
    c. if the data type of the two variables are different then throws an error
    """

    return  x + y

print(fun1("Hello", "World"))

print("=" * 40)

help(fun1)
