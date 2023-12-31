import multiprocessing
import time
import concurrent.futures
from unittest import result

multiprocessing.set_start_method("fork")

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second")
    time.sleep(seconds)
    return f"Done Sleeping....{seconds}"

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())


#Method 1 for implementing multiprocessing
# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()


# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")