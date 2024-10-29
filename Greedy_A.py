import heapq

graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'S': 1, 'C': 2, 'D': 5},
    'B': {'S': 4, 'D': 1},
    'C': {'A': 2, 'D': 1, 'G': 3},
    'D': {'A': 5, 'B': 1, 'C': 1, 'G': 2},
    'G': {}
}

heuristics = {
    'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 4, 'G': 0
}

def a_star(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (h[start], start))
    came_from = {start: None}
    g_score = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current
    return []

print("A* Path:", a_star(graph, 'S', 'G', heuristics))
