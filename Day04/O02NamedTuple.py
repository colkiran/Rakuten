
# immutable dictionary , creating a class using functions
def Set_marks(p, c, b, m, e):
    from collections import namedtuple

    nmdTpl = namedtuple("Marks", "phy che bio maths eng")
    marks = nmdTpl(phy=p, che=c, bio=b, maths=m, eng=e)
    return marks

mrk = Set_marks(89, 94, 99, 96, 85)
print(mrk)

print(f"Physics   :{mrk.phy}")
print(f"Chemistry :{mrk.che}")
print(f"Biology   :{mrk.bio}")
print(f"Maths     :{mrk.maths}")
print(f"English   :{mrk.eng}")
