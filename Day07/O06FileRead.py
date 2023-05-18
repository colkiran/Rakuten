"""
 opening the file in read mode and its the default mode

 read - reads the entire content of the file
 read(250) - mention the bytes and it reads the specified number of bytes

 readline - can read one line at a time
 readline(byte) - bytes mentioned should be less than the line size

 readlines - reads all the lines and stores it in a list
 readlines(50) - read that entire line where the 50th byte falls

"""

FL = open("data.txt", "r")

# st = FL.read(1200)

# st = FL.readline(900)

st = FL.readlines(950)

# print(st)
for i in st:
    print(i)

FL.close()