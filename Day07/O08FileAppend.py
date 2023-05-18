
"""

adds contents into the existing file without disturbing the contents already present in the file

"""

FA = open("myfile.txt", "a")

st = input("Enter the contents of the file :")

FA.write(st + "\n")

FA.close()