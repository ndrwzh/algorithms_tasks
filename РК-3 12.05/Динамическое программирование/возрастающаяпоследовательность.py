def findLIS(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    dp = [1] * len(nums)  # Инициализируем dp-массив единицами
    max_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
            max_length = max(max_length, dp[i])

    return max_length