def copy_time(n, x, y):
    if n <= 1:
        return 0
    n -= 1
    left = 0
    right = n * min(x, y)  
    while left <= right:
        mid = (left + right) // 2
        copies = mid // x + mid // y
        if copies >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left


