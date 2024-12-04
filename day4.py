import util
import numpy as np
from typing import List
"""
Key point: handle 2D matrix
1. numpy usage: np.transpose(), arr.diagonal(), np.fliplr()
2. matrix array slicing
Start to use python3 format with argument type
"""
def parse_input() -> List[List[str]]:
    """Parses the puzzle input into a 2D matrix of characters.

    Returns:
        A 2D list where each inner list represents a row of characters from the input.
    """
    puzzle_input = util.get_input_data(4)
    return [list(line.strip()) for line in puzzle_input.split("\n")]

def get_count_xmas() -> int:
    """Counts occurrences of 'XMAS' and 'SAMX' in rows, columns, and diagonals.

    Returns:
        Total count of 'XMAS' and 'SAMX' patterns in the matrix.
    """
    matrix = np.array(parse_input())
    transposed_matrix = np.transpose(matrix)
    diagonals_matrix = get_diagonals(matrix)
    
    total_count = (
        count_string(matrix) + 
        count_string(transposed_matrix) + 
        count_string(diagonals_matrix)
    )
    return total_count

def count_string(matrix: np.ndarray) -> int:
    """Counts occurrences of 'XMAS' and 'SAMX' in a given matrix.

    Args:
        matrix: A numpy array of characters.

    Returns:
        Number of 'XMAS' and 'SAMX' patterns found.
    """
    return sum(
        "".join(row).count("XMAS") + 
        "".join(row).count("SAMX") 
        for row in matrix
    )

def get_diagonals(matrix: np.ndarray) -> List[np.ndarray]:
    """Extracts all diagonals (main and anti-diagonals) from a matrix.

    Args:
        matrix: A 2D numpy array.

    Returns:
        A list of diagonal arrays including both main and anti-diagonals.
    """
    main_diagonals = [matrix.diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    anti_diagonals = [np.fliplr(matrix).diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    return main_diagonals + anti_diagonals

def get_real_count_xmax() -> int:
    """Counts special 'XMAX' formations in the matrix.

    A valid formation requires an 'A' at the center with specific surrounding 
    patterns of 'M' and 'S' characters.

    Returns:
        Number of valid 'XMAX' formations found.
    """
    matrix = parse_input()
    n, m = len(matrix), len(matrix[0])
    
    def is_valid_xmax_pattern(i: int, j: int) -> bool:
        """Check if the surrounding pattern around matrix[i][j] is valid."""
        surrounding = [
            (i-1, j-1), (i-1, j+1), 
            (i+1, j-1), (i+1, j+1)
        ]
        
        patterns = [
            ['M', 'M', 'S', 'S'],
            ['M', 'S', 'M', 'S'],
            ['S', 'S', 'M', 'M'],
            ['S', 'M', 'S', 'M']
        ]
        
        chars = [matrix[x][y] for x, y in surrounding]
        return matrix[i][j] == 'A' and chars in patterns
    
    return sum(
        is_valid_xmax_pattern(i, j)
        for i in range(1, n - 1)
        for j in range(1, m - 1)
    )

def main():
    print(get_count_xmas())
    print(get_real_count_xmax())

if __name__ == "__main__":
    main()