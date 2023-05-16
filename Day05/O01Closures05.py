
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)
    return innerFun


outerFun("Welcome")('Sachin')

inRef = outerFun("Welcome")
# after few lines
print("Hello World \n" * 5)
# simple curry
print("-" * 40)
inRef("Rahul")
inRef("Sourav")
inRef('Yuvraj')

print("-" * 40)
tmlGrt = outerFun("Vanakam")
tmlGrt("Dhoni")
tmlGrt("Ashwin")
