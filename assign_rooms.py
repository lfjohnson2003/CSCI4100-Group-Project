def assign_rooms(time_slot_assignment, rooms):
    used_rooms_per_slot = {}
    final_schedule = {}

    for course, slot in time_slot_assignment.items():
        used = used_rooms_per_slot.get(slot, set())
        available = next((room for room in rooms if room not in used), None)
        if available:
            used_rooms_per_slot.setdefault(slot, set()).add(available)
            final_schedule[course] = (slot, available)
        else:
            final_schedule[course] = (slot, "No Room Available")
    return final_schedule
