
glbX = 100          # global variable

def fun(a):         # a is a local variable
    global glbX     # cannot assign a value in this line
    print(f"The value of a inside is :{a}")
    b = a * 2       # local var
    glbX = 500
    print(f"glbX inside :{glbX}")

    print(f"b :{b}")

print(f"before glbX :{glbX}")

fun(50)

print(f"after glbX :{glbX}")
