import time
import random
import tracemalloc

def search_target_using_binary_search(elements , target):
    left = 0
    right = len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        if elements[middle] == target:
            return middle
        elif elements[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def test_binary_search_on_data(elements , target):
    start = time.perf_counter()
    tracemalloc.start()

    result = search_target_using_binary_search(elements,target)

    current , peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    end = time.perf_counter()

    return {
        "is_Element_found" : result != -1,
        "target_index": result,
        "time_taken": end - start,
        "memory_used": peak
    }
    

n = 100000 # Dataset size

sorted_data = list(range(n))
reversed_sorted_data = list(range(n-1,-1,-1))
random_data = sorted(random.sample(range(1, n * 2), n))

target = random_data[n//2]

results = {
    "sorted_dataset":test_binary_search_on_data(sorted_data,target),
    "reverse_dataset":test_binary_search_on_data(reversed_sorted_data,target),
    "random_dataset":test_binary_search_on_data(random_data,target)
}

print("Data set size ",n)
for typedata, metrics in results.items():
    print(f"--- {typedata} Dataset ---")
    print(f"Found: {metrics['is_Element_found']} at index: {metrics['target_index']}")
    print(f"Time Taken: {metrics['time_taken']:.6f} seconds")
    print(f"Peak Memory Used: {metrics['memory_used']} bytes")
    print()
