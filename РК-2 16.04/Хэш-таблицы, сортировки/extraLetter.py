def extra_letter(a: str, b: str) -> str:
    hash_map_a = {}
    for char in a:
        hash_map_a[char] = hash_map_a.get(char, 0) + 1
    
    for char in b:
        if char in hash_map_a:
            hash_map_a[char] -= 1
            if hash_map_a[char] == 0:
                del hash_map_a[char]
        else:
            return char
    
    return ""