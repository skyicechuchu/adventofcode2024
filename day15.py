import numpy as np

def parse_input(input_text):
    map_lines = input_text.split('\n\n')[0].split('\n')
    moves_lines = input_text.split('\n\n')[1].replace('\n', '')
    
    map_array = np.array([list(line) for line in map_lines])
    
    robot_pos = tuple(np.where(map_array == '@'))
    robot_pos = (robot_pos[0][0], robot_pos[1][0])
    
    return map_array, robot_pos, moves_lines

def print_map(map_array):

    print('\n'.join([''.join(row) for row in map_array]))
    print('\n')

def is_valid_move(map_array, pos):
    return map_array[pos[0], pos[1]] not in ['#']

def calculate_gps_coordinates(map_array):
    box_positions = list(zip(*np.where(map_array == 'O')))
    return sum(100 * pos[0] + pos[1] for pos in box_positions)

def push_boxes(map_array, start_pos, direction):
    dy, dx = direction
    current_pos = start_pos
    
    box_chain = [current_pos]
    
    while True:
        next_pos = (current_pos[0] + dy, current_pos[1] + dx)
        
        # If next position is a wall, can't move
        if not is_valid_move(map_array, next_pos):
            return False
        # If next position is a box, continue the chain
        if map_array[next_pos[0], next_pos[1]] == 'O':
            box_chain.append(next_pos)
            current_pos = next_pos
        # If next position is empty, we can push
        elif map_array[next_pos[0], next_pos[1]] == '.':
            break
        # If something unexpected is found, can't move
        else:
            return False
    
    # Now actually move the boxes
    # Work backwards through the chain
    for i in range(len(box_chain) - 1, -1, -1):
        current_box = box_chain[i]
        new_box_pos = (current_box[0] + dy, current_box[1] + dx)
        
        map_array[current_box[0], current_box[1]] = '.'
        
        # Place the box in its new position
        map_array[new_box_pos[0], new_box_pos[1]] = 'O'
    
    return True

def move_robot(map_array, robot_pos, move):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    
    dy, dx = directions[move]
    new_robot_pos = (robot_pos[0] + dy, robot_pos[1] + dx)
    

    # print(f"Move {move}:")
    # print_map(map_array)
    
    # Check if new robot position is a wall
    if not is_valid_move(map_array, new_robot_pos):
        return robot_pos, map_array
    
    if map_array[new_robot_pos[0], new_robot_pos[1]] == 'O':
        if not push_boxes(map_array, new_robot_pos, directions[move]):
            return robot_pos, map_array
    
    map_array[robot_pos[0], robot_pos[1]] = '.'
    map_array[new_robot_pos[0], new_robot_pos[1]] = '@'
    
    return new_robot_pos, map_array

def solve_warehouse_puzzle(input_text):
    map_array, robot_pos, moves = parse_input(input_text)
    
    print("Initial state:")
    print_map(map_array)
    
    for move in moves:
        robot_pos, map_array = move_robot(map_array, robot_pos, move)
    
    print("Final state:")
    print_map(map_array)
    
    return calculate_gps_coordinates(map_array)

def main():
    input_text = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

    input_text2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
    import util
    input_text = util.get_input_data(15)
    result = solve_warehouse_puzzle(input_text)
    print(f"\nSum of GPS coordinates: {result}")

if __name__ == "__main__":
    main()