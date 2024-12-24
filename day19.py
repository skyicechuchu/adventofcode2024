def can_make_design(patterns, design):
    n = len(design)
    dp = [False] * (n + 1)
    dp[n] = True
    
    for i in range(n-1, -1, -1):
        for pattern in patterns:
            if i + len(pattern) <= n:
                matches = True
                for j in range(len(pattern)):
                    if design[i + j] != pattern[j]:
                        matches = False
                        break
                if matches and dp[i + len(pattern)]:
                    dp[i] = True
                    break
    
    return dp[0]

def solve_towel_puzzle(input_text):
    lines = input_text.strip().split('\n')
    patterns = [pattern.strip() for pattern in lines[0].split(',')]
    
    designs = []
    for line in lines[2:]:
        if line.strip():
            designs.append(line.strip())
    
    possible_count = 0
    for design in designs:
        if can_make_design(patterns, design):
            possible_count += 1
    
    return possible_count

def count_arrangements(patterns, design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[n] = 1
    
    for i in range(n-1, -1, -1):
        for pattern in patterns:
            if i + len(pattern) <= n:
                matches = True
                for j in range(len(pattern)):
                    if design[i + j] != pattern[j]:
                        matches = False
                        break
                if matches:
                    dp[i] += dp[i + len(pattern)]
    
    return dp[0]

def solve_towel_puzzle_2(input_text):
    lines = input_text.strip().split('\n')
    patterns = [pattern.strip() for pattern in lines[0].split(',')]
    
    designs = []
    for line in lines[2:]:
        if line.strip():
            designs.append(line.strip())
    
    total_arrangements = 0
    for design in designs:
        arrangements = count_arrangements(patterns, design)
        total_arrangements += arrangements
    
    return total_arrangements

example_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

result = solve_towel_puzzle(example_input)
print(f"Number of possible designs: {result}")  # Should print 6
result = solve_towel_puzzle_2(example_input)
print(f"\nTotal arrangements: {result}")  # Should print 16

import util
input_data = util.get_input_data(19)
result = solve_towel_puzzle(input_data)
print(f"Number of possible designs: {result}")  # Should print 360
result = solve_towel_puzzle_2(input_data)
print(f"\nTotal arrangements:: {result}")  # Should print 577474410989846

