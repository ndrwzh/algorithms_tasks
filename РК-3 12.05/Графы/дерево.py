from collections import deque

def is_tree(graph, start_node=0):

    num_nodes = len(graph)
    visited = set()
    queue = deque([start_node])
    parent = {start_node: None}

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            elif parent.get(vertex) != neighbor:  # Проверка на цикл
                return False

    return len(visited) == num_nodes  # Проверка на связность