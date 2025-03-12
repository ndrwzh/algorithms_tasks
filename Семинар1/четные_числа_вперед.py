def rearrange_array(arr):
    n = len(arr)
    even_index = 0  

    for i in range(n):
        if arr[i] % 2 == 0: 
            if i != even_index:
                arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1 

    return arr

