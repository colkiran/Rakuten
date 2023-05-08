
a = 10
b = -10


print(f"a :{a}")            # f - format string - interpolation
print(type(a))              # rtti - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 10.0
d = -10.0
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)
e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(d))

print("-" * 40)
g =  3+4j
h =  3-4j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)
x = 2 + 3.5
print(type(x))

print("-" * 40)
x = 1
y = 2.5
z = x + y
print(f"x :{type(x)}")
print(f"y :{type(y)}")
print(f"z :{type(z)}")

print("conversion".center(40, "-"))
x = 100
print(f"{type(x)}\t\t{x}")
print(f"{type(float(x))}\t\t{float(x)}")
print(f"{type(complex(x))}\t\t{complex(x)}")
print(f"{type(bool(x))}\t\t{bool(x)}")

print("Number System".center(40, "-"))
print(11)                       # decimal
print(f"0b11  :{0b11}")           # binary
print(f"0b101 :{0b101}")          # binary
print(f"0o11  :{0o11}")           # octal
print(f"0o101 :{0o101}")          # octal
print(f"0xe   :{0xe}")            # hexa
print(f"0xa   :{0xa}")            # hexa

print("Conversion".center(40, "-"))
a = 100
print(f"bin :{bin(a)}")
print(f"oct :{oct(a)}")
print(f"hex :{hex(a)}")
