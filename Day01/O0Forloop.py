
for i in range(1, 11):
    print(i, end=" ")

print()
for i in range(20, 10, -1):
    print(i, end=" ")

print()
for i in range(2, 15, 2):
    print(i, end=" ")

# continue, break and else
print()
print("-" * 40)
for i in range(1, 20):
    if i % 2 == 1:
        continue            # skip the iteration
    # if i > 15:
    #     break               # skip the current loop
    print(i, end= " ")
else:
    print("\ncompleted the iteration")
