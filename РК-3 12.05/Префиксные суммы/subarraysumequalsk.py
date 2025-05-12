def subarray_sum(nums, k):

    prefix_sum = 0
    prefix_count = {0: 1}  # Словарь для хранения префиксных сумм и их количеств
    count = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count