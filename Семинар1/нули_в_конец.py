def move_zeros_to_end(arr):
    n = len(arr)
    write_index = 0
    for i in range(n):
        if arr[i] != 0:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, n):
        arr[i] = 0

    return arr