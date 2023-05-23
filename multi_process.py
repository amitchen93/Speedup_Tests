import concurrent.futures
import time
from functools import partial


def heavy_cpu_func(limit: int = 5, printout: bool = False):
    """ a function that simulates a CPU-heavy task """
    res = 0
    for i in range(limit):
        i += 1
        res += i
    if (printout):
        print("done")
    return res


def call_func_normally(limit: int = 15000, printout: bool = False):
    sum = 0
    for i in range(limit):
        result = heavy_cpu_func(limit, printout)
        sum += result
    return sum


def map_func_concurrently(limit: int = 15000, printout: bool = False, max_workers: int = 5):
    sum = 0
    cpu_func = partial(heavy_cpu_func, printout=printout)
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(cpu_func, range(limit))
    for num in results:
        sum += num
    return sum


if __name__ == '__main__':
    # start = time.time()
    # # call_func_normally(15000, False)
    # map_func_concurrently(15000, False)
    # end = time.time()
    # print(f"took {end - start} seconds")
    times = dict()
    for num in range(2, 8):
        start = time.time()
        map_func_concurrently(limit=30000, printout=False, max_workers=num)
        end = time.time()
        times[num] = end - start
    print(times)