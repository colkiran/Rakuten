
def funLogger(fnc):
    def helper():
        print("Myinfo logged into a service......")
        fnc()
        print("Myinfo logged out of the service......")
    return helper

def normalfun():
    print("Call me a normal function")

print("-" * 40)
funLogger(normalfun)        #no ouput
print("-" * 40)
funLogger(normalfun)()      # calls the helper function
print("-" * 40)
res_fun = funLogger(normalfun)
res_fun()

print("-" * 40)
normalfun = funLogger(normalfun)
normalfun()

print("-" * 40)
@funLogger                  # decorator
def basicfun():
    print("Call me as Basic function.....")

# basicfun = funLogger(basicfun)
basicfun()