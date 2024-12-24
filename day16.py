from heapq import heappush, heappop
from dataclasses import dataclass
from typing import List, Set, Tuple, Dict
from collections import defaultdict

@dataclass(frozen=True, order=True)
class State:
    x: int
    y: int
    direction: Tuple[int, int]  # (dx, dy)

def parse_maze(input_str: str) -> Tuple[List[List[str]], State, Tuple[int, int]]:
    maze = [list(line) for line in input_str.strip().split('\n')]
    start = None
    end = None
    
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                start = (x, y)
            elif maze[y][x] == 'E':
                end = (x, y)
                
    return maze, State(start[0], start[1], (1, 0)), end

def get_rotations(current_dir: Tuple[int, int]) -> List[Tuple[int, int]]:
    if current_dir == (1, 0):   # East
        return [(0, -1), (0, 1)]  # North, South
    elif current_dir == (-1, 0): # West
        return [(0, -1), (0, 1)]  # North, South
    elif current_dir == (0, 1):  # South
        return [(1, 0), (-1, 0)]  # East, West
    else:                        # North
        return [(1, 0), (-1, 0)]  # East, West

def find_min_score(maze: List[List[str]], start_state: State, end: Tuple[int, int]) -> int:
    height, width = len(maze), len(maze[0])
    queue = [(0, start_state)]
    visited = {start_state: 0}
    
    while queue:
        score, state = heappop(queue)
        
        if (state.x, state.y) == end:
            return score
            
        # Forward movement
        new_x = state.x + state.direction[0]
        new_y = state.y + state.direction[1]
        
        if (0 <= new_x < width and 0 <= new_y < height and 
            maze[new_y][new_x] != '#'):
            new_state = State(new_x, new_y, state.direction)
            new_score = score + 1
            
            if new_state not in visited or visited[new_state] > new_score:
                visited[new_state] = new_score
                heappush(queue, (new_score, new_state))
        
        # Rotations
        for new_dir in get_rotations(state.direction):
            new_state = State(state.x, state.y, new_dir)
            new_score = score + 1000
            
            if new_state not in visited or visited[new_state] > new_score:
                visited[new_state] = new_score
                heappush(queue, (new_score, new_state))
    
    return float('inf')

def find_optimal_tiles(maze: List[List[str]], start_state: State, end: Tuple[int, int], min_score: int) -> int:
    height, width = len(maze), len(maze[0])
    optimal_tiles = set()
    queue = [(0, start_state, {(start_state.x, start_state.y)})]
    visited = defaultdict(lambda: float('inf'))
    visited[start_state] = 0
    
    while queue:
        score, state, path_tiles = heappop(queue)
        
        if score > min_score:
            continue
            
        if (state.x, state.y) == end and score == min_score:
            optimal_tiles.update(path_tiles)
            continue
            
        # Forward movement
        new_x = state.x + state.direction[0]
        new_y = state.y + state.direction[1]
        
        if (0 <= new_x < width and 0 <= new_y < height and 
            maze[new_y][new_x] != '#'):
            new_state = State(new_x, new_y, state.direction)
            new_score = score + 1
            new_path = path_tiles | {(new_x, new_y)}
            
            if new_score <= min_score and new_score <= visited[new_state]:
                visited[new_state] = new_score
                heappush(queue, (new_score, new_state, new_path))
        
        # Rotations
        for new_dir in get_rotations(state.direction):
            new_state = State(state.x, state.y, new_dir)
            new_score = score + 1000
            
            if new_score <= min_score and new_score <= visited[new_state]:
                visited[new_state] = new_score
                heappush(queue, (new_score, new_state, path_tiles))
    
    return len(optimal_tiles)

def solve_maze(input_str: str) -> Tuple[int, int]:
    maze, start_state, end = parse_maze(input_str)
    min_score = find_min_score(maze, start_state, end)
    optimal_tiles = find_optimal_tiles(maze, start_state, end, min_score)
    return min_score, optimal_tiles

# Test with examples
example1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()

example2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()

score1, tiles1 = solve_maze(example1)
print(f"Example 1 - Score: {score1}, Optimal tiles: {tiles1}")  # Should be 7036, 45

score2, tiles2 = solve_maze(example2)
print(f"Example 2 - Score: {score2}, Optimal tiles: {tiles2}")  # Should be 11048, 64

import util
input = util.get_input_data(16).strip()
score, titles = solve_maze(input)
print(f"Input - Score: {score}, Optimal tiles: {titles}")
