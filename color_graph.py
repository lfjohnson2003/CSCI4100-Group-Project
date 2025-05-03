# Assigns time slots (represented as colors) to nodes (courses) using a greedy graph coloring algorithm.
# Ensures no two adjacent nodes (conflicting courses) share the same time slot.

def color_graph(graph):
    # Dictionary to store the assigned color (time slot) for each node (course)
    color_assignment = {}

    # Sort nodes to ensure deterministic and repeatable coloring order
    nodes = sorted(graph.keys())

    # Iterate through each node in the graph
    for node in nodes:
        # Collect the colors already used by neighboring nodes (conflicting courses)
        neighbor_colors = set()
        for neighbor in graph[node]:
            if neighbor in color_assignment:
                neighbor_colors.add(color_assignment[neighbor])

        # Find the smallest non-conflicting color (time slot)
        color = 0
        while color in neighbor_colors:
            color += 1

        # Assign the selected color to the current node
        color_assignment[node] = color

    # Return the final color (time slot) assignment for all nodes (courses)
    return color_assignment
