def pascals_triangle(n):
    if n <= 0:
        return []  # Обработка некорректного ввода

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Создаем строку, заполненную единицами
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle