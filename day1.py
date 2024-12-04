import util
import collections

"""
Algo key point:
1. sort algo: using the native Python sort. It takes O(nlogn). Need know write
from scratch on Merge-sort, Quick-sort
2. hash counter: O(n), get counts on listB, then A get frequency is O(1)
"""

def parse_input():
    """Parses the raw puzzle input into two lists of integers.

    Splits the input by lines, then splits each line into two integers, which are added
    to separate lists.

    Returns:
        tuple: A tuple containing two lists of integers (list_a, list_b).
    """
    puzzle_input = util.get_input_data(1)
    list_a = []
    list_b = []
    for line in puzzle_input.split("\n"):
        numbers = line.strip().split("   ")  # Assuming three spaces as delimiter
        list_a.append(int(numbers[0]))
        list_b.append(int(numbers[1]))
    return list_a, list_b

def get_total_distance(a, b):
    """Calculates the total absolute distance between corresponding elements of two lists.

    The lists are first sorted, then the absolute differences between each pair of elements
    are summed.

    Args:
        a (list of int): First list of integers.
        b (list of int): Second list of integers.

    Returns:
        int: The total absolute distance between the two lists.
    """
    res = 0
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    for i in range(len(a_sorted)):
        res += abs(a_sorted[i] - b_sorted[i])
    return res

def get_similarity_score(a, b):
    """Calculates a similarity score between two lists.

    For each number in list 'a', counts how many times it appears in list 'b', and multiplies
    the number by that count.

    Args:
        a (list of int): First list of integers.
        b (list of int): Second list of integers.

    Returns:
        int: The similarity score.
    """
    b_counts = collections.Counter(b)
    return sum(num * b_counts[num] for num in a)

if __name__ == "__main__":
    list_a, list_b = parse_input()
    print(get_total_distance(list_a, list_b))
    print(get_similarity_score(list_a, list_b))
