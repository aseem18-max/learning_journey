# Memoization - A term used in Computer Science which means to store so that it can be subsequently retrieved without repeating the computation.
from functools import lru_cache
from time import sleep, time
@lru_cache(maxsize = None)
def fx(n):
    sleep(5)
    return n*5
a = time()
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
print(time()-a)
b = time()
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
print(time()-b)