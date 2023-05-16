
def bank_flow(fnc):         # HOF
    print("-" * 40)
    print("Logging into the server.........")
    fnc()                   # callback
    print("Logging out of the server.......")
    print("-" * 40)

def deposit():
    print("Amount ###### credited into the account......")

def withdraw():
    print("Amount ###### debited from the account.......")


bank_flow(deposit)
bank_flow(withdraw)

