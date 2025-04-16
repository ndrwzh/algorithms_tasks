from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)  # Словарь для хранения групп анаграмм
    
    for word in strs:
        # Сортируем буквы слова и используем как ключ
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    # Возвращаем значения словаря в виде списка списков
    return list(anagrams.values())

