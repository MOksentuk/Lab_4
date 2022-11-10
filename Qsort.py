l = [3, 2, 4, 1, 6, 8, 5, 8]
l1 = [5, 4, 6]


def step(l):
    m = l[0]
    SmallerThanm = []
    BiggerThanm = []
    for i in range(1, len(l)):
        if l[i] < m:
            SmallerThanm.append(l[i])
        elif l[i] >= m:
            BiggerThanm.append(l[i])
    SmallerThanm.append(m)
    if len(SmallerThanm) <= 2 and len(BiggerThanm) <= 1:
        res = SmallerThanm + BiggerThanm
        return SmallerThanm, BiggerThanm
    else:
        step(SmallerThanm)
        step(BiggerThanm)


def qsort(l):
    a,b=step(l)


print(step(l1))
