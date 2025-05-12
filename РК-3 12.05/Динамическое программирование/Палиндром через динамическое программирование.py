def longestPalindromeDP(s):

    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]  # Инициализируем DP-массив
    max_len = 1
    start = 0

    # Базовый случай: все символы сами по себе являются палиндромами
    for i in range(n):
        dp[i][i] = True

    # Проверяем подстроки длины 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i

    # Проверяем подстроки длины 3 и больше
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    max_len = k
                    start = i

    return s[start : start + max_len]





