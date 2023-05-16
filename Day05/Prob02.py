import time

def timeCalc(fnc):
    def innerFun(arg):
        st = time.time()
        fnc(arg)
        et = time.time()
        print(f"The total time taken by the function to execute is :{round(et-st, 2)} secs")
    return innerFun


@timeCalc
def fun(x):
    l = []
    for i in range(1, x+1):
        for j in range(1, i+ 1):
            l.append(j ** 2)

fun(5500)
