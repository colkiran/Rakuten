
st = "Hello World"
print(F"st :{st}")
print(type(st))

print("-" * 40)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("slicing".center(40, "-"))
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("Reverse Indexing".center(40, "-"))
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("Slicing".center(40, "-"))
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# code to check if the string is a palindrome
print("-" * 40)
# st = input("Enter a string :")
st = "abba"
print('Palindrome :' + st if st[:] == st[::-1] else 'Not a Palindrome :' + st)
print("True" if st[:] == st[::-1] else "Not a Palidrome")

# functions to manipulate a string
print("-" * 40)
st = "hello world"
print(f"st :{st}")
# st[0] = "H"
# print(dir(st))

print("find".center(40, "-"))
st = "hello world"
pos = st.find("w")
print(f"pos :{pos}")

pos = st.find("e")
print(f"pos :{pos}")

pos = st.find("l")
print(f"pos :{pos}")

pos = st.find("l",st.find("l", st.find("l")+1)+1)
print(f"pos :{pos}")

print("replace".center(40, "-"))
st = "hello world"
print(f"st :{st}")
res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")
