import time
import random
import tracemalloc

def merge_sort(elements):
    if len(elements) <= 1:
        return elements
    
    mid = len(elements) // 2
    first_half = merge_sort(elements[:mid])
    second_half = merge_sort(elements[mid:])
    
    return merge(first_half,second_half)

def merge(array1 , array2):
    result = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result.extend(array1[i:])
    result.extend(array2[j:])
    return result

def test_merge_sort_on_elements(elements):
    start = time.perf_counter()
    tracemalloc.start()

    sorted_result = merge_sort(elements)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.perf_counter()

    return {
        "is_sorted": sorted_result == sorted(elements),
        "time_taken": end - start,
        "memory_used": peak
    }


# Dataset size
n = 100000

sorted_data = list(range(n))
reversed_sorted_data = list(range(n-1, -1, -1))
random_data = random.sample(range(1, n * 2), n)

results = {
    "sorted_dataset": test_merge_sort_on_elements(sorted_data),
    "reverse_dataset": test_merge_sort_on_elements(reversed_sorted_data),
    "random_dataset": test_merge_sort_on_elements(random_data)
}

print("Data Set Size " ,n)

for typedata, metrics in results.items():
    print(f"--- {typedata} Dataset ---")
    print(f"Sorted Correctly: {metrics['is_sorted']}")
    print(f"Time Taken: {metrics['time_taken']:.6f} seconds")
    print(f"Peak Memory Used: {metrics['memory_used']} bytes")
    print()