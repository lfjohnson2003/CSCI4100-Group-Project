def print_schedule(schedule):
    for course, (slot, room) in sorted(schedule.items()):
        print(f"Course: {course} | Time Slot: {slot} | Room: {room}")
