
import sys

num = 10
div = 0
try:
    res = num / div
    print(f'res :{res}')

except:
    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
