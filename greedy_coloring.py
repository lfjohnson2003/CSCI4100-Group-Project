def greedy_coloring(graph):
    color_assignment = {}
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = {color_assignment[neighbor] for neighbor in graph[node] if neighbor in color_assignment}
        for color in range(len(graph)):
            if color not in neighbor_colors:
                color_assignment[node] = color
                break
    return color_assignment
