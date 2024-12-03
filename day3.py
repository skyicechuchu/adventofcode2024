import util
import re

"""
"""

def get_input_data():
    aoc_session = util.login_advent_of_code()
    if aoc_session:
        day = 3
        input_url = f'https://adventofcode.com/2024/day/{day}/input'
        input_response = aoc_session.get(input_url)
        puzzle_input = input_response.text.strip()
        return puzzle_input
    else:
        return ""

def parse_input():
    puzzle_input = get_input_data()
    dataset = []
    for line in puzzle_input.split("\n"):
        dataset.append(line.strip())
    return dataset

def get_multiplications():
    """
    Calculates the sum of all multiplications found in the input data,
    where each multiplication is defined by 'mul(a,b)' with a and b being 1-3 digit numbers.

    Returns:
        int: The total sum of all multiplications.
    """
    dataset = parse_input()
    if not dataset:
        return 0

    total = 0
    pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
    for line in dataset:
        matches = pattern.findall(line)
        for a_str, b_str in matches:
            a, b = int(a_str), int(b_str)
            total += a * b
    return total

def get_multiplications_with_instructions():
    """
    Calculates the sum of multiplications while obeying 'do()' and 'don't()' instructions.
    Multiplications are ignored after 'don't()' and resumed after 'do()'.

    Returns:
        int: The total sum of applicable multiplications.
    """
    dataset = parse_input()
    if not dataset:
        return 0

    total = 0
    pattern = re.compile(r"(mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|do(?:n't)?\(\))")
    mul_pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")

    ignore = False
    for line in dataset:
        tokens = pattern.findall(line)
        for token in tokens:
            if token == "don't()":
                ignore = True
            elif token == "do()":
                ignore = False
            elif not ignore:
                match = mul_pattern.match(token)
                if match:
                    a, b = int(match.group(1)), int(match.group(2))
                    total += a * b
    return total

if __name__ == "__main__":
    print("Total without instructions:", get_multiplications())
    print("Total with instructions:", get_multiplications_with_instructions())

