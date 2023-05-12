
# non local variables

def ourterFun():
    gst = "Sachin"

    def innerFun():
        nonlocal  gst
        gst = "Mr." + "Rahul"               # local var
        print("Hello World")
        print(gst)

    innerFun()
    print(f"After :{gst}")

ourterFun()

