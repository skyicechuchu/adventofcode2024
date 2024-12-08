"""
Module for analyzing antenna antinodes in a grid-based map.

This module provides functionality to generate and count antinodes 
in a grid map with antenna positions.

Functions:
    generate_antinodes: Prepares the antinode grid and antenna locations.
    find_antinodes_q1: Identifies antinodes using the first method.
    find_antinodes_q2: Identifies antinodes using the second method.
"""

import itertools
import util

def generate_antinodes(map_input: str):
    """
    Generate antenna locations and prepare the antinode grid.

    Args:
        map_input (str): A string representation of the antenna map,
            where '.' represents empty space and other characters 
            represent antenna locations.

    Returns:
        tuple: A 4-tuple containing:
            - antinodes (List[List[int]]): A 2D grid of antinode markers.
            - antennas (Dict[str, List[Tuple[int, int]]]): Dictionary of 
              antenna locations grouped by their identifier.
            - m (int): Number of rows in the grid.
            - n (int): Number of columns in the grid.
    """
    antennas = {}
    rows = map_input.strip().split('\n')
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                antennas.setdefault(char, []).append((x, y))

    m, n = len(rows), len(rows[0])
    antinodes = [[0] * n for _ in range(m)]

    return antinodes, antennas, m, n


def find_antinodes_q1(map_input: str) -> int:
    """
    Find antinodes using the first method.

    Identifies points in the grid that are symmetrically positioned 
    relative to antenna pairs.

    Args:
        map_input (str): A string representation of the antenna map.

    Returns:
        int: Total number of unique antinode points.
    """
    antinodes, antennas, m, n = generate_antinodes(map_input)

    for coords in antennas.values():
        for (x1, y1), (x2, y2) in itertools.permutations(coords, 2):
            dx, dy = x2 - x1, y2 - y1
            nx, ny = x1 - dx, y1 - dy
            if 0 <= nx < n and 0 <= ny < m:
                antinodes[ny][nx] = 1

    return sum(map(sum, antinodes))


def find_antinodes_q2(map_input: str) -> int:
    """
    Find antinodes using the second method.

    Identifies points in the grid that are symmetrically positioned 
    relative to antenna pairs, with extended tracing.

    Args:
        map_input (str): A string representation of the antenna map.

    Returns:
        int: Total number of unique antinode points.
    """
    antinodes, antennas, m, n = generate_antinodes(map_input)

    for coords in antennas.values():
        for (x1, y1), (x2, y2) in itertools.permutations(coords, 2):
            dx, dy = x2 - x1, y2 - y1
            nx, ny = x1, y1
            while True:
                nx, ny = nx - dx, ny - dy
                if 0 <= nx < n and 0 <= ny < m:
                    antinodes[ny][nx] = 1
                else:
                    break
            antinodes[y1][x1] = 1

    return sum(map(sum, antinodes))


def main():
    """
    Main execution function to run antinode analysis.

    Prints the results of both antinode finding methods using 
    input data from the utility module.
    """
    input_data = util.get_input_data(8)
    print("Q1 Antinodes Count:", find_antinodes_q1(input_data))
    print("Q2 Antinodes Count:", find_antinodes_q2(input_data))


if __name__ == '__main__':
    main()
