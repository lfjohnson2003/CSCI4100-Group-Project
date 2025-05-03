# Import necessary functions for scheduling:
from color_graph import color_graph
from assign_rooms import assign_rooms
from print_schedule import print_schedule

# Helper: Convert edge list to adjacency list
def build_adjacency_list(edges):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph

# Main execution block
if __name__ == "__main__":
    # Define conflict edges
    conflict_edges = [
        ('C1', 'C2'),  # Same Professor
        ('C1', 'C3'),  # Same Room
        ('C2', 'C4'),  # Same Time Slot
        ('C3', 'C5'),  # Same Students
        ('C4', 'C6'),  # Same Time Slot
        ('C5', 'C6')   # Same Professor
    ]

    # List of available rooms
    rooms = ['101', '102', '103', '104']

    # Build adjacency list
    conflict_graph = build_adjacency_list(conflict_edges)

    # Assign time slots using backtracking
    time_slot_assignment = color_graph(conflict_graph)

    # Assign rooms
    final_schedule = assign_rooms(time_slot_assignment, rooms)

    # Print initial schedule
    print("Initial Schedule:")
    print_schedule(final_schedule)

    # Add new course C7 with conflicts
    conflict_edges.extend([
        ('C7', 'C1'),
        ('C7', 'C4')
    ])
    conflict_graph = build_adjacency_list(conflict_edges)

    # Reassign time slots and rooms
    time_slot_assignment = color_graph(conflict_graph)
    final_schedule = assign_rooms(time_slot_assignment, rooms)

    # Print final schedule
    print("\nUpdated Schedule with C7:")
    print_schedule(final_schedule)
