import heapq #для работы с минимальной кучей

def merge_k_sorted_arrays(sorted_arrays):
    
    merged_array = []
    min_heap = []
    

    for array_idx, array in enumerate(sorted_arrays):
        if len(array) > 0:

            heapq.heappush(min_heap, (array[0], array_idx, 0))
    

    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(value)
        
        if element_idx + 1 < len(sorted_arrays[array_idx]):
            next_value = sorted_arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, array_idx, element_idx + 1))
    
    return merged_array