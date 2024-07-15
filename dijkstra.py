def dijkstra(graph, start, end):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    visited = set()
    nodes_to_process = [start]
    min_distance = float('inf')
    current_node = None
    
    while nodes_to_process:
        for node in nodes_to_process:
            if distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        current_node = min(nodes_to_process, key=lambda node: distances[node])
        nodes_to_process.remove(current_node)
        
        if current_node == end:
            return distances[current_node]
        
        for neighbour, weight in graph[current_node]:
            if neighbour not in visited:
                new_weight = distances[current_node] + weight
                if new_weight < distances[neighbour]:
                    distances[neighbour] = new_weight
                nodes_to_process.append(neighbour)
                
        visited.add(current_node)
            
            
        
        
# Example graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

# Calculate the shortest distance from 'A' to 'F'
shortest_distance = dijkstra(graph, 'A', 'F')
print(shortest_distance)  # Output should be 13
