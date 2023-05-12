
def outerFun():
    gst = 'Mr. Sachin'

    def innerFun():
        gst1 = "Mr. Rahul"
        print('hello world')
        print(gst1)
        print(gst)

    return innerFun             # HOF - higher order function


inRef = outerFun()
inRef()
