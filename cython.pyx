
def cfunc(int n):
    cdef int a = 0
    for i in range(n):
        a += i
    return a

print cfunc(10)