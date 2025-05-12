import sys

def coinChange(coins, amount):
    
    dp = [sys.maxsize] * (amount + 1)  # Инициализируем dp-массив максимальным значением
    dp[0] = 0  # Базовый случай: для суммы 0 нужно 0 монет

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == sys.maxsize:
        return -1  # Сумма недостижима
    else:
        return dp[amount]
