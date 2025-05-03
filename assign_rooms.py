# Assigns rooms to courses based on their assigned time slots.
# Ensures that no room is double-booked within the same time slot.

def assign_rooms(time_slot_assignment, rooms):
    # Dictionary to track which rooms have already been assigned in each time slot
    used_rooms_per_slot = {}

    # Dictionary to hold the final schedule: course -> (time slot, room)
    final_schedule = {}

    # Iterate through each course and its assigned time slot
    for course, slot in time_slot_assignment.items():
        # Get the set of rooms already used in this time slot (default to empty set)
        used = used_rooms_per_slot.get(slot, set())

        # Find the first available room not already used in this time slot
        available = next((room for room in rooms if room not in used), None)

        if available:
            # Mark the room as used for this time slot
            used_rooms_per_slot.setdefault(slot, set()).add(available)

            # Assign the room to the course
            final_schedule[course] = (slot, available)
        else:
            # If no rooms are available, mark the course with "No Room Available"
            final_schedule[course] = (slot, "No Room Available")

    # Return the complete schedule with time slots and assigned rooms
    return final_schedule
