
"""
No of  Males and females

unique list of departments

unique list of desigs

sum of all salaries

"""
FL = open("EMP.csv", "r")

lines = FL.readlines()

gen = {}
des = []
dep = []
sal = 0

for line in lines:
    # print(line)

    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]

    if g not in gen:
        gen[g] = 1
    else:
        gen[g] += 1

    if ds not in des:
        des.append(ds)

    if dp not in dep:
        dep.append(dp)

    sal += int(line.split(",")[5])

FL.close()

print(gen)
print(des)
print(dep)
print(sal)
