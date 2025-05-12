def max_subarray_sum(arr, k):

    n = len(arr)
    if n < k:
        return None

    current_sum = sum(arr[:k])  # Сумма первого окна
    max_sum = current_sum

    for i in range(k, n):
        current_sum = current_sum - arr[i - k] + arr[i]  # Скользящее окно
        max_sum = max(max_sum, current_sum)

    return max_sum