
def outerFun():

    def innerFun():
        print('hello world')

    return innerFun

outerFun()()            # calls the innerFun

print("-" * 40)
inRef = outerFun()
inRef()