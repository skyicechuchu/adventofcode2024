from collections import deque
from typing import List, Tuple, Set

def parse_coordinates(input_data: str) -> List[Tuple[int, int]]:
    """Parse the input string into a list of coordinate tuples."""
    coordinates = []
    for line in input_data.strip().split('\n'):
        if line:
            x, y = map(int, line.strip().split(','))
            coordinates.append((x, y))
    return coordinates

def create_corrupted_set(coordinates: List[Tuple[int, int]], num_bytes: int, grid_size: int) -> Set[Tuple[int, int]]:
    corrupted = set()
    for x, y in coordinates[:num_bytes]:
        if 0 <= x < grid_size and 0 <= y < grid_size:
            corrupted.add((x, y))
    return corrupted

def find_shortest_path(grid_size: int, corrupted: Set[Tuple[int, int]]) -> int:
    """
    Find the shortest path from (0,0) to (grid_size-1, grid_size-1) 
    using BFS, avoiding corrupted coordinates.
    """
    if (0, 0) in corrupted or (grid_size-1, grid_size-1) in corrupted:
        return -1  
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}
    
    while queue:
        x, y, steps = queue.popleft()
        
        if x == grid_size-1 and y == grid_size-1:
            return steps
            
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 <= new_x < grid_size and 
                0 <= new_y < grid_size and 
                (new_x, new_y) not in corrupted and 
                (new_x, new_y) not in visited):
                    queue.append((new_x, new_y, steps + 1))
                    visited.add((new_x, new_y))
    
    return -1

def solve_memory_pathfinding(input_data: str, num_bytes: int = 1024, grid_size: int = 71) -> int:
    """Main solving function."""
    coordinates = parse_coordinates(input_data)
    corrupted = create_corrupted_set(coordinates, num_bytes, grid_size)
    shortest_path = find_shortest_path(grid_size, corrupted)
    
    return shortest_path

def is_path_possible(grid_size: int, corrupted: Set[Tuple[int, int]]) -> bool:
    """
    Check if there is a path from (0,0) to (grid_size-1, grid_size-1) 
    avoiding corrupted coordinates.
    """
    if (0, 0) in corrupted or (grid_size-1, grid_size-1) in corrupted:
        return False
    
    # right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    
    while queue:
        x, y = queue.popleft()
        
        if x == grid_size-1 and y == grid_size-1:
            return True
            
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 <= new_x < grid_size and 
                0 <= new_y < grid_size and 
                (new_x, new_y) not in corrupted and 
                (new_x, new_y) not in visited):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
    
    return False

def find_first_blocking_byte(coordinates: List[Tuple[int, int]], grid_size: int) -> Tuple[int, int]:
    """Find the first byte that makes the path impossible."""
    corrupted = set()
    
    for _, (x, y) in enumerate(coordinates):
        corrupted.add((x, y))
        
        if not is_path_possible(grid_size, corrupted):
            return x, y
    
    return -1, -1


example_data = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
"""

example_result = solve_memory_pathfinding(example_data, num_bytes=12, grid_size=7)
print(f"Example result (should be 22): {example_result}")

import util
input_data = util.get_input_data(18)

actual_result = solve_memory_pathfinding(input_data, num_bytes=1024, grid_size=71)
print(f"Actual result: {actual_result}")

example_coords = parse_coordinates(example_data)
example_x, example_y = find_first_blocking_byte(example_coords, 7)
print(f"Example blocking byte (should be 6,1): {example_x},{example_y}")

coords = parse_coordinates(input_data)
x, y = find_first_blocking_byte(coords, 71)
print(f"First blocking byte: {x},{y}")