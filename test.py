import timeit as t

qsort = 'for i in range(1000000): pass'
print(qsort)
print(t.timeit(stmt=qsort, number=1))
