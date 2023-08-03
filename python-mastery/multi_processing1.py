from glob import glob
import multiprocessing

multiprocessing.set_start_method("fork")

# result = []
# 

# Below methos is not working because memory is not shared between
# processes by default so we need to make changes to function
# def calc_square(numbers):
#     global result
#     for n in numbers:
#         result.append(n*n)
#     print("Inside process: "+str(result))

def calc_square(numbers, result, v):
    v.value = 5.57
    for idx, n in enumerate(numbers):
        result[idx] = n*n


if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers,result, v))
    p.start()
    p.join()

    print(f"Outside process: {result[:]}")
    print(v.value)