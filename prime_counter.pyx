cimport cython


@cython.cdivision(True)
cpdef prime_count_cy(range_from: int, range_til: int):
    """ Returns the number of found prime numbers using range"""
    cdef int prime_count = 0
    cdef int num
    cdef int divnum
    range_from = range_from if range_from >= 2 else 2
    for num in range(range_from, range_til + 1):
        for divnum in range(2, num):
            if ((num % divnum) == 0):
                break
        else:
            prime_count += 1
    return prime_count
    # Terminal command to build the .pyx file: python setup.py build_ext --inplace
