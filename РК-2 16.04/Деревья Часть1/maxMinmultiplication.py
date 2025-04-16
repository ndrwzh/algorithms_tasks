def max_min_multiplication(data):
    if len(data) < 3:
        return -1
    
    min_index = 0
    while 2 * min_index + 1 < len(data):
        min_index = 2 * min_index + 1
        if data[min_index] is None:  # Проверка на None-значения
            break
    
    max_index = 0
    while 2 * max_index + 2 < len(data):
        max_index = 2 * max_index + 2
        if data[max_index] is None:  # Проверка на None-значения
            break
    
    # Проверка что значения существуют и не None
    if min_index >= len(data) or max_index >= len(data) or data[min_index] is None or data[max_index] is None:
        return -1
    
    return data[min_index] * data[max_index]