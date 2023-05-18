
"""
Position = FL.seek(bytes, whence)

whence - 0 - BOF
         1 - CP
         2 - EOF

"""
FL = open("data.txt", "rb")

pos =FL.seek(50, 0)          # 50 count from BOF

print(f"position :{pos}")

pos =FL.seek(50, 1)          # 50 count from CP

print(f"position :{pos}")

pos =FL.seek(50, 2)          # 50 count from EOF

print(f"position :{pos}")

pos =FL.seek(0, 2)

print(f"position :{pos}")

pos =FL.seek(-100, 2)

print(f"position :{pos}")

FL.close()