# Import necessary functions for scheduling:
from greedy_coloring import greedy_coloring
from assign_rooms import assign_rooms
from print_schedule import print_schedule

# Main execution block
if __name__ == "__main__":
    # Define the list of courses
    courses = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

    # Define the conflict graph where edges represent scheduling conflicts between courses
    conflict_graph = {
        'C1': ['C2', 'C3'],
        'C2': ['C1', 'C4'],
        'C3': ['C1', 'C5'],
        'C4': ['C2', 'C6'],
        'C5': ['C3', 'C6'],
        'C6': ['C4', 'C5']
    }

    # List of available rooms
    rooms = ['101', '102', '103', '104']

    # Step 1: Assign time slots to courses using greedy coloring to avoid conflicts
    time_slot_assignment = greedy_coloring(conflict_graph)

    # Step 2: Assign rooms to courses based on their time slots
    final_schedule = assign_rooms(time_slot_assignment, rooms)

    # Step 3: Print the initial course schedule
    print("Initial Schedule:")
    print_schedule(final_schedule)

    # Add a new course C7 and define its conflicts
    print("\nUpdated Schedule with C7:")
    conflict_graph['C7'] = ['C1', 'C4']
    conflict_graph['C1'].append('C7')
    conflict_graph['C4'].append('C7')

    # Recalculate time slots and room assignments with the updated graph
    time_slot_assignment = greedy_coloring(conflict_graph)
    final_schedule = assign_rooms(time_slot_assignment, rooms)

    # Print the updated schedule including the new course
    print_schedule(final_schedule)
