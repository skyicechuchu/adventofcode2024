import util

"""
Q1: the time is O(mn)
Q2: the time is O(mn^2)
Algo key point: operate the list, remove a element, all(), any(), zip()
"""

def parse_input():
    puzzle_input = util.get_input_data(2)
    reports= []
    for line in puzzle_input.split("\n"):
        levels = line.strip().split(" ")
        levels = [int(i) for i in levels]
        reports.append(levels)
    return reports

def get_safe_reports():
    return sum(1 for each in parse_input() if is_safe(each))

def is_safe(levels):
    if not levels or len(levels) == 0:
        return False
    
    if len(levels) == 1:
        return True
    
    is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels)-1))
    is_decreasing = all(levels[i+1] < levels[i] for i in range(len(levels)-1))

    if not (is_increasing or is_decreasing):
        return False
    
    for i in range(len(levels) - 1):
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False
    return True

def get_safe_reports_with_damper():
    data_set = parse_input()
    safe_count = sum(is_safe_with_damper(report) for report in data_set)
    return safe_count


def is_safe_with_damper(levels):
    if is_safe(levels):
        return True
    
    for i in range(len(levels)):
        if i > 0 and i < len(levels) - 1:
            if (abs(levels[i - 1] - levels[i]) >= 1 and 
                abs(levels[i - 1] - levels[i]) <= 3) and \
                (abs(levels[i] - levels[i + 1]) >= 1 and abs(levels[i] - levels[i + 1]) <= 3):
                if abs(levels[i - 1] - levels[i + 1]) < 1 or \
                    abs(levels[i - 1] - levels[i + 1]) > 3:
                    continue
        new_levels = levels[:i] + levels[i + 1:]
        increasing = all(new_levels[j] < new_levels[j + 1] for j in range(len(new_levels) - 1))
        decreasing = all(new_levels[j] > new_levels[j + 1] for j in range(len(new_levels) - 1))
        
        if increasing or decreasing:
            valid = True
            for j in range(len(new_levels) - 1):
                diff = abs(new_levels[j] - new_levels[j + 1])
                if diff < 1 or diff > 3:
                    valid = False
                    break
            if valid:
                return True
    
    return False


print(get_safe_reports())
print(get_safe_reports_with_damper())