# CSCI4100-Group-Project

The objective of this project is to use Graph Coloring to solve scheduling and resource allocation problems. By representing tasks or resources as nodes and conflicts 
(like overlapping times or shared resources) as edges, we can assign colors (or distinct resources) to each node to ensure no conflicts. Assign the minimum color to 
each node that doesn’t conflict with its neighbors.

## Group Members

Logan Johnson  
Kyle Peterson

## How It Works

There are 4 Python files in this project:

### `main.py`
This is the main script that ties everything together. It:
- Defines course conflicts (same professor, same students, etc.).
- Builds a conflict graph.
- Uses a greedy coloring algorithm to assign time slots.
- Assigns rooms so there are no overlaps in the same time slot.
- Prints the schedule before and after adding a new course (C7).

### `color_graph.py`
Handles the **time slot assignment**. It uses a greedy graph coloring algorithm:
- Each course is a node.
- If two courses conflict, they get different "colors" (a.k.a. time slots).
- Greedy = fast but not guaranteed to be optimal.

### `assign_rooms.py`
Takes the time slots and assigns rooms to courses:
- Makes sure no two courses share the same room at the same time.
- If all rooms are taken in a time slot, the course gets `"No Room Available"`.

### `print_schedule.py`
Just formats and prints the final schedule so it's readable:
