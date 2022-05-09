import threading
import time

p = 0
def count_time():
    global p
    time_start = time.time()
    while p != 1:
        time.sleep(1)
        print(str(int(time.time() - time_start)) + " seconds")


thread1 = threading.Thread(target=count_time, args=())

k = 1
pi = 0

thread1.start()
for i in range(10000000):
    if i % 2 == 0:
        pi += 4/k
    else:
        pi -= 4/k
    
    k += 2

p = 1
thread1.join()
print(pi)