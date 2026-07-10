import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
a = time.time()
func(4)
func(2)
func(1)
print(time.time() - a)

#Same code using threading
b = time.time()
t1 = threading.Thread(target = func, args = [4])
t2 = threading.Thread(target = func, args = [2])
t3 = threading.Thread(target = func, args = [4])

t1.start()
t2.start()
t3.start()
print(time.time()-b)