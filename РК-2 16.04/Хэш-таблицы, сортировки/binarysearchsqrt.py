def binary_search_sqrt(target):
    if target < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен.")
    if target == 0:
        return 0
    low = 0
    high = target
    while low <= high:
        mid = (low + high) // 2  
        square = mid * mid
        if square == target:
            return mid
        elif square < target:
            low = mid + 1
        else:
            high = mid - 1
    return high if (high * high) <= target else low

