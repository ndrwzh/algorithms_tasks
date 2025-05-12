def is_bipartite(graph):

    num_nodes = len(graph)
    colors = [0] * num_nodes  # 0 - непосещенная, 1 - цвет 1, -1 - цвет -1

    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == 0:
                if not dfs(neighbor, -color):
                    return False
            elif colors[neighbor] == color:
                return False  # Конфликт цветов
        return True

    for i in range(num_nodes):
        if colors[i] == 0:
            if not dfs(i, 1):
                return False

    return True