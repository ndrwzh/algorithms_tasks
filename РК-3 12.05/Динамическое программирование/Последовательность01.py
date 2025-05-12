def b_sequences(n):
    if n <= 0:
        return 0  # Обработка некорректного ввода
    elif n == 1:
        return 2  # Базовый случай: 0 или 1
    elif n == 2:
        return 3  # Базовый случай: 00, 01, 10

    dp = [0] * (n + 1)
    dp[1] = 2
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
