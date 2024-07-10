def a_star(graph, start, end, heuristic):
    import heapq
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path = {}
    heuristics = {node: heuristic(node, end) for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight + heuristics[neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path[neighbor] = current_node
    return distances, shortest_path
