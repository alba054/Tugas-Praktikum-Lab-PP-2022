def _max(*args):
    newList = list(args)
    nilaiBesar = 0
    for i in newList:
        nilaiBesar = i if i > nilaiBesar else nilaiBesar
        for j in newList:
            if i is j:
                continue
            if i > nilaiBesar and i > j:
                nilaiBesar = i
    return(nilaiBesar)

_max(12,23,4,5,6)