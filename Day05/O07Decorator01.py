
def funlogger(fnc):
    def helper(x, y):
        print("Myinfo logged into a service.....")
        print(fnc(x, y))
        print("Myinfo logged out of the service.....")
        print("=" * 40)
    return helper

@funlogger
def add(a, b):
    print('Add called.....')
    return a + b

@funlogger
def sub(a, b):
    print("Sub called.....")
    return a - b

add(65, 58)
sub(59, 34)
