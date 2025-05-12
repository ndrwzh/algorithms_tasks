def color_connected_components(graph):

    num_nodes = len(graph)
    visited = {i: 0 for i in range(1, num_nodes + 1)}  # Инициализация словаря с нулевыми цветами
    color = 0

    def dfs(node, current_color):
        visited[node] = current_color
        for neighbor in graph.get(node, []):
            if visited[neighbor] == 0:
                dfs(neighbor, current_color)

    for node in range(1, num_nodes + 1):
        if visited[node] == 0:
            color += 1
            dfs(node, color)

    return visited