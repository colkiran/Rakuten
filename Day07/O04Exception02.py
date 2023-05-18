
inv = 1
num = "0"

try:
    inv = 1 / num
# except ZeroDivisionError as z:
#     print(z)
# except TypeError as t:
#     print(t)
except Exception as e:
    print(e)
else:
    print(f"inv :{inv}")
finally:
    print("The division of numbers completed.......")
