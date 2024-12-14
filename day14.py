import util
from collections import Counter
import matplotlib.pyplot as plt

def parse_input(input_text):
    robots = []
    for line in input_text.strip().split('\n'):
        # Extract position and velocity
        pos_part, vel_part = line.split(' ')
        x = int(pos_part.split('=')[1].split(',')[0])
        y = int(pos_part.split('=')[1].split(',')[1])
        vx = int(vel_part.split('=')[1].split(',')[0])
        vy = int(vel_part.split('=')[1].split(',')[1])
        robots.append((x, y, vx, vy))
    return robots

def simulate_robots(robots, width, height, time):

    final_positions = []
    for px, py, vx, vy in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        final_positions.append((final_x, final_y))
    return final_positions

def calculate_safety_factor_by_quadrant(positions, width, height):
    quadrants = Counter()

    half_width = width // 2
    half_height = height // 2
    
    for px, py in positions:
        if px == half_width or py == half_height:
            continue
        quadrants[(px < width // 2, py < height // 2)] += 1
    
    safety_factor = 1
    for v  in quadrants.values():
        safety_factor *= v
    return safety_factor
    

def calculate_safety_factor(quadrant_counts):

    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count
    return safety_factor

def solve_q1(input_text, width=101, height=103, time=100):

    robots = parse_input(input_text)
    
    final_positions = simulate_robots(robots, width, height, time)
    return calculate_safety_factor_by_quadrant(final_positions, width, height)

def count_horizontal_adjacencies(positions, width, height):
    adjacencies = 0
    pos_set = set(positions)
    for y in range(height):
        for x in range(width - 1):
            if (x, y) in pos_set and (x + 1, y) in pos_set:
                adjacencies += 1
    return adjacencies

def solve_q2(input_text, width=101, height=103):
    final_time = 0
    robots = parse_input(input_text)
    for time in range(10000):
        positions = simulate_robots(robots, width, height, time)
        adjacencies = count_horizontal_adjacencies(positions, width, height)
        if adjacencies > 80: # tune the parameter by visualize plot
            final_time = time
            coordinates = positions
            break
    return final_time, coordinates

def plot(coordinates):

    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]

    plt.figure(figsize=(12, 8))
    plt.scatter(x_coords, y_coords, alpha=0.6)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    example_input = util.get_input_data(14)
    safety_factor = solve_q1(example_input)
    time, coordinates = solve_q2(example_input)
    plot(coordinates)
    print(f"Safety Factor: {safety_factor}")
    print(f"Times: {time}")