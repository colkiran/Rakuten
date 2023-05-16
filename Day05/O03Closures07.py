
def log_details(fnc):           # takes a function as argument
    logInfo = "Logging into the server......."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(50, 65)
diff_logger(50, 35)
