import primes
import concurrent.futures
from time import time


def prime_count(range_from: int, range_til: int):
    """ Returns the number of found prime numbers using range"""
    prime_count = 0
    range_from = range_from if range_from >= 2 else 2
    for num in range(range_from, range_til + 1):
        for divnum in range(2, num):
            if ((num % divnum) == 0):
                break
        else:
            prime_count += 1
    return prime_count


def chunk_ranges(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        end = i + n if i + n < len(l) else len(l)
        yield i, end


def call_prime_count_concurrently(range_from: int, range_till: int, max_workers: int = 5):
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as exe:
        futures = list()
        chunks = list(chunk_ranges(l=[x for x in range(range_from, range_till)], n=max_workers))
        for fr, to in chunks:
            prime_sum = exe.submit(primes.prime_count_cy, fr, to)
            futures.append(prime_sum)
    total_prime_sum = sum(item.result() for item in futures)
    return total_prime_sum


if __name__ == '__main__':
    # start_regular = time()
    # res_regular = prime_count(0, 200000)
    # end_regular = time()
    # print(f"Total time for regular call in seconds: {end_regular - start_regular}")
    start = time()
    res_cython = primes.prime_count_cy(0, 1000000)
    end = time()
    print(f"Total time for cython call in seconds: {end - start}")
    start = time()
    x = call_prime_count_concurrently(range_from=0, range_till=1000000, max_workers=12)
    end = time()
    print(f"Total time for cython multiprocessed call in seconds: {end-start}")
    # Terminal command to build the .pyx file: python setup.py build_ext --inplace
