def summa_from_n1_to_n2(n_1, n_2):
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1 

    p_1 = n_1
    p_2 = n_2
    summa = 0

    while p_1 <= p_2:
        summa += p_1
        if p_1 != p_2:
            summa += p_2
        p_1 += 1
        p_2 -= 1

    return summa