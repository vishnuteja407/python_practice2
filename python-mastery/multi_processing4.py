from array import array
import multiprocessing
import time

def f(n):
    sum = 0
    for x in range(100):
        sum += x*x
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = multiprocessing.Pool(processes=3)
    result = p.map(f, range(10000))
    p.close()
    p.join()

    print("Pool took:", time.time()-t1)

    result = []
    for x in range(10000):
        result.append(f(x))
    
    t2 = time.time()
    print("Serial processing took", time.time()-t2)