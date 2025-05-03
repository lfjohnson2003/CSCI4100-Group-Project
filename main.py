from greedy_coloring import greedy_coloring
from assign_rooms import assign_rooms
from print_schedule import print_schedule

if __name__ == "__main__":
    courses = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
    conflict_graph = {
        'C1': ['C2', 'C3'],
        'C2': ['C1', 'C4'],
        'C3': ['C1', 'C5'],
        'C4': ['C2', 'C6'],
        'C5': ['C3', 'C6'],
        'C6': ['C4', 'C5']
    }

    rooms = ['101', '102', '103', '104']

    time_slot_assignment = greedy_coloring(conflict_graph)
    final_schedule = assign_rooms(time_slot_assignment, rooms)

    print("Initial Schedule:")
    print_schedule(final_schedule)

    print("\nUpdated Schedule with C7:")
    conflict_graph['C7'] = ['C1', 'C4']
    conflict_graph['C1'].append('C7')
    conflict_graph['C4'].append('C7')

    time_slot_assignment = greedy_coloring(conflict_graph)
    final_schedule = assign_rooms(time_slot_assignment, rooms)

    print_schedule(final_schedule)
