def can_make_valid_with_deletions(s, k):
    
    balance = 0
    extra_closed = 0  # Количество лишних закрывающих скобок

    for char in s:
        if char == '(':
            balance += 1
        elif balance > 0:  # Если есть открывающие скобки, закрываем их
            balance -= 1
        else:  # Если нет открывающих скобок, это лишняя закрывающая
            extra_closed += 1

    return extra_closed <= k