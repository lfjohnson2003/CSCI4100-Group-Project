from collections import defaultdict

class CourseScheduler:
    def __init__(self):
        self.courses = set()
        self.conflicts = defaultdict(set)
        self.time_slot_groups = []
        self.available_rooms = [101, 102, 103, 104, 105]
        self.room_constraints = defaultdict(set)  # Tracks which courses must share rooms

    def add_course(self, course_id):
        self.courses.add(course_id)

    def add_conflict(self, conflict_type, course1, course2):
        if conflict_type == "Same professor" or conflict_type == "Same student group":
            self.conflicts[course1].add(course2)
            self.conflicts[course2].add(course1)
        elif conflict_type == "Same room":
            # Mark these courses to share the same room
            self.room_constraints[course1].add(course2)
            self.room_constraints[course2].add(course1)
        elif conflict_type == "Same time slot required":
            added = False
            for group in self.time_slot_groups:
                if course1 in group or course2 in group:
                    group.update([course1, course2])
                    added = True
                    break
            if not added:
                self.time_slot_groups.append({course1, course2})

    def greedy_coloring(self):
        color_assignment = {}
        current_color = 0

        # Process time slot groups first
        for group in self.time_slot_groups:
            used_colors = set()
            for course in group:
                for neighbor in self.conflicts[course]:
                    if neighbor in color_assignment:
                        used_colors.add(color_assignment[neighbor])
            
            group_color = 0
            while group_color in used_colors:
                group_color += 1
            
            for course in group:
                color_assignment[course] = group_color

        # Color remaining courses
        remaining = sorted([c for c in self.courses if c not in color_assignment],
                         key=lambda x: -len(self.conflicts[x]))
        
        for course in remaining:
            used_colors = {color_assignment[n] for n in self.conflicts[course] 
                         if n in color_assignment}
            color = 0
            while color in used_colors:
                color += 1
            color_assignment[course] = color

        return color_assignment

    def assign_rooms(self, color_assignment):
        schedule = []
        time_slot_rooms = defaultdict(set)
        room_assignments = {}  # Track final room assignments
        
        # First pass: assign rooms to courses with room constraints
        for course in sorted(self.courses):
            if course in self.room_constraints and course not in room_assignments:
                time_slot = color_assignment[course]
                
                # Find a room that works for all courses in this room group
                room = None
                for r in self.available_rooms:
                    if r not in time_slot_rooms[time_slot]:
                        # Check if this room works for all constrained courses
                        valid = True
                        for other in self.room_constraints[course]:
                            if other in room_assignments and room_assignments[other] != r:
                                valid = False
                                break
                        if valid:
                            room = r
                            break
                
                if room is None:
                    room = next(r for r in self.available_rooms 
                              if r not in time_slot_rooms[time_slot])
                
                # Assign this room to all constrained courses
                room_assignments[course] = room
                time_slot_rooms[time_slot].add(room)
                for other in self.room_constraints[course]:
                    if other not in room_assignments:
                        room_assignments[other] = room
                        if color_assignment[other] == time_slot:
                            time_slot_rooms[time_slot].add(room)

        # Second pass: assign rooms to remaining courses
        for course in sorted(self.courses):
            if course not in room_assignments:
                time_slot = color_assignment[course]
                room = next(r for r in self.available_rooms 
                          if r not in time_slot_rooms[time_slot])
                room_assignments[course] = room
                time_slot_rooms[time_slot].add(room)
        
        # Build final schedule
        for course in sorted(self.courses):
            schedule.append({
                'course': course,
                'time_slot': color_assignment[course],
                'room': room_assignments[course]
            })
        
        return schedule

def input_courses(scheduler):
    print("\n=== Enter Courses ===")
    while True:
        course = input("Enter course ID (or 'done'): ").strip().upper()
        if course == 'DONE':
            break
        scheduler.add_course(course)

def input_conflicts(scheduler):
    conflict_types = {
        '1': 'Same professor',
        '2': 'Same student group',
        '3': 'Same room',
        '4': 'Same time slot required'
    }
    
    print("\n=== Enter Conflicts ===")
    while True:
        print("\nConflict types:")
        for num, desc in conflict_types.items():
            print(f"{num}. {desc}")
        print("5. Done with conflicts")
        
        choice = input("Select conflict type (1-5): ").strip()
        if choice == '5':
            break
            
        if choice not in conflict_types:
            print("Invalid choice")
            continue
            
        print(f"Enter courses with {conflict_types[choice]} conflict:")
        course1 = input("First course: ").strip().upper()
        course2 = input("Second course: ").strip().upper()
        
        if course1 not in scheduler.courses or course2 not in scheduler.courses:
            print("Error: One or both courses don't exist")
            continue
            
        scheduler.add_conflict(conflict_types[choice], course1, course2)

def print_schedule(schedule):
    print("\n=== Final Schedule ===")
    print("{:<8} {:<12} {:<8}".format(
        "Course", "Time Slot", "Room"))
    for item in schedule:
        print("{:<8} {:<12} {:<8}".format(
            item['course'],
            f"TS-{item['time_slot']}",
            item['room']
        ))

def main():
    scheduler = CourseScheduler()
    input_courses(scheduler)
    input_conflicts(scheduler)
    
    color_assignment = scheduler.greedy_coloring()
    schedule = scheduler.assign_rooms(color_assignment)
    print_schedule(schedule)

if __name__ == "__main__":
    main()
