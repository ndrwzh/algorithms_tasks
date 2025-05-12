def find_connected_components(graph):

    num_nodes = len(graph)
    visited = [False] * (num_nodes + 1)  # Индексация с 1
    connected_components = []

    def dfs(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph.get(node, []):  # Обработка случая отсутствия ключа
            if not visited[neighbor]:
                dfs(neighbor, component)

    for node in range(1, num_nodes + 1):
        if not visited[node]:
            component = []
            dfs(node, component)
            connected_components.append(component)

    return connected_components