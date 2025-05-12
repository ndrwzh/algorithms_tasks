def count_sequences(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 4

    dp = [1, 2, 4]  # Базовые случаи для n=0, 1, 2
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    return dp[n]

