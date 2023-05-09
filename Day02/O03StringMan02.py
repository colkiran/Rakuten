
# join, split, maketrans, translate

print("split".center(40, "-"))
st = "emp001, Sachin, 34, 450, Australia"
print(f"st :{st}")
res = st.split(", ")
print(type(res))
print(f"res :{res}")

emp = ",".join(res)
print(f'emp :{emp}')
print(type(emp))

print("maketrans".center(40, "-"))
st = "hello world"
print(f"st: {st}")
a = 'helowrd'
b = "HELOWRD"
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

res = st.translate(resTbl)
print(f"res :{res}")
