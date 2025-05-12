def maxProfit(prices):
    if not prices:
        return 0  # Обработка пустого списка

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)  # Обновляем минимальную цену
        max_profit = max(max_profit, price - min_price) # Обновляем максимальную прибыль

    return max_profit