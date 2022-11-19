import timeit as tt
import Functions

start_time = tt.default_timer()
d = [12, 5, 6, 23, 75, 8, 34, 6, 2, 1]
print(Functions.Qsort(d))
print(tt.default_timer() - start_time)
start_time = tt.default_timer()
print(Functions.combsort(d))
print(tt.default_timer() - start_time)
