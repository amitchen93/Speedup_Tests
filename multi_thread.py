import concurrent.futures
import time
from functools import partial


def heavy_io_func(some_value: int, printout: bool=False):
    """ A function that simulates an IO heavy task """
    time.sleep(2)
    if (printout):
        print('done')
    return some_value * 2


def call_func_normally(max_num: int = 5, printout: bool = False):
    sum = 0
    for num in range(max_num):
        result = heavy_io_func(some_value=max_num, printout=printout)
        sum += result
    return sum


def call_func_concurrently(max_num: int = 5, printout: bool = False):
    sum = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = list()
        for num in range(max_num):
            result = executor.submit(heavy_io_func, some_value=num, printout=printout)
            futures.append(result)
        for num in concurrent.futures.as_completed(futures):
            sum += num.result()
    return sum


def map_func_concurrently(max_num: int = 5, printout: bool = False):
    io_func = partial(heavy_io_func, printout=printout)
    sum = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(io_func, range(max_num))
        for num in results:
            sum += num
    return sum


if __name__ == '__main__':
    start = time.time()
    # call_func_normally(5, True)
    call_func_concurrently(5, True)
    # map_func_concurrently(5, False)
    end = time.time()
    print(f"took {end - start} seconds")
