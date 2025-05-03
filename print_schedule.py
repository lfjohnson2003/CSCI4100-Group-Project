# Prints the schedule in a readable format.
# Each course is displayed with its assigned time slot and room.

def print_schedule(schedule):
    # Iterate over the schedule items in sorted order by course name
    for course, (slot, room) in sorted(schedule.items()):
        # Print the course details in a formatted string
        print(f"Course: {course} | Time Slot: {slot} | Room: {room}")
