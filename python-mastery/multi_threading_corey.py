import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} seconds....")
    time.sleep(seconds)
    return f"Done Sleeping....{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    #method 1 for threading implementation
    # results = [executor.submit(do_something, sec) for sec in secs]
    
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    #method 2 for threading implementation
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")
