def Qsort(mass):
    if len(mass) <= 1:
        return mass
    else:
        pillar = mass[0]
        SmallerThanPillar = []
        EqualPillar = []
        BiggerThanPillar = []
        for el in mass:
            if el < pillar:
                SmallerThanPillar.append(el)
            elif el > pillar:
                BiggerThanPillar.append(el)
            else:
                EqualPillar.append(el)
        return Qsort(SmallerThanPillar) + EqualPillar + Qsort(BiggerThanPillar)

def combsort(l):
    ll = len(l)
    for i in range(ll-1):
        for j in range(i+1):
            f,s=l[j], l[-1*(i + 1)+j]
            if f > s:
                l[j], l[-1*(i + 1)+j] = s, f
    return l
