def has_cycle(graph):
   
    num_nodes = len(graph)
    visited = set()  # Используем множество для более эффективной проверки принадлежности

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor != parent:
                if neighbor in visited:
                    return True  # Цикл обнаружен
                if dfs(neighbor, node):
                    return True  # Цикл обнаружен в подграфе
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):  # Запускаем DFS от каждой непосещенной вершины
                return True

    return False