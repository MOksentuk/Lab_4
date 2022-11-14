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