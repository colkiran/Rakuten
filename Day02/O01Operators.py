
print("Arithmetic Operators".center(40, "-"))
print(f"10 + 3 = {10 + 3}")           # sum
print(f"10 - 3 = {10 - 3}")           # sub
print(f"10 * 3 = {10 * 3}")           # multi
print(f"10 / 3 = {10 / 3}")           # div
print(f"10 // 3 = {10 // 3}")         # flr div
print(f"10 % 3 = {10 % 3}")           # Mod
print(f"10 ** 3 = {10 ** 3}")         # Exp


print("Augmentor Operator".center(40, "-"))
# =, +=, -=, *=, /=

x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x //= 3
print(f"x :{x}")

print("Comparison Operators".center(40, "-"))
# ==, !=, >, >=, <, <=
print(f"1 == 1 :{1 == 1}")
print(f"2 == 1 :{2 == 1}")
print(f"2 != 1 :{2 != 1}")
print(f"2 >= 1 :{2 >= 1}")

print("Logical Operators".center(40,"-"))
# and, or, not
print(f" 1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f" 1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
print(f" 1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f" not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")

print("-" * 40)
print(f"ord('A') :{ord('A')}")  # integer representation of unicode characters
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print("-" * 40)
print(f"'apple' > 'orange' :{'apple' > 'orange'}")
print(f"'apple' < 'orange' :{'apple' < 'orange'}")

print('Bitwise Operators'.center(40, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")

print(f"5 >> 1 :{5 >> 1}")
print(f"16 >> 1 :{16 >> 1}")

print("Ternary Operator".center(40, "-"))
a = 19
print("Eligible" if a >= 18 else "Not Eligible")
