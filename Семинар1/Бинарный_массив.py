def sort_binary_array(nums):
    
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == 1 and nums[right] == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        elif nums[left] == 0:
            left += 1
        elif nums[right] == 1:
            right -= 1