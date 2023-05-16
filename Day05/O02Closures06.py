
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun
    return innerFun

KanGrt = outerFun("Namaskara")
KanTgr = KanGrt("tiger")
KanTgr("Prabhakar")

KanGrt = outerFun("Namaskara")
KanLion = KanGrt("lion")
KanLion("Prabhakar")


"""
engGrt = outerFun("Welcome")
sarwEgrt = engGrt("----->")
dblarwEgrt = engGrt("======>>")

hndGrt = outerFun("Namaskar")
sarwHgrt = hndGrt("------>")
dblarwHgrt = hndGrt("======>>")

sarwEgrt("Mr.Sachin")
dblarwEgrt("Mr.Rahul")

sarwHgrt("Mr. Jadeja")
dblarwHgrt("Mr. Sunil")
"""