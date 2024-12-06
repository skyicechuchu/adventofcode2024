import util
from collections import defaultdict, deque
"""
Q1: I use Topological Sort, then there is no head (in-degree=0) node which means it is no DAG.
Then I just build dependency graph as a hashmap. Build the dependency graph is O(m+n), then valid the page using this hash map.
Each query in graph will be O(1) and n times operation for all pages. O(n)
Q2: use bubble sort O(n^2), this should improve with merge sort. I will do later.

"""

def parse_input():
    puzzle_input = util.get_input_data(5)
    dependency = []
    page_numbers = []
    for line in puzzle_input.split("\n"):
        if "|" in line:
            dependency.append(line)
        if "," in line:
            page_numbers.append(line)
    
    return dependency, page_numbers

# def get_topo_sorting():
#     dependency, _ = parse_input()
#     adj = set()
#     graph = defaultdict(set)
#     in_degree = defaultdict(int)
#     for each in dependency:
#         before, after = map(int, each.split('|'))
#         adj.add(before)
#         adj.add(after)
#         if after not in graph[before]:
#             graph[before].add(after)
#             in_degree[after] += 1
#             if before not in in_degree:
#                 in_degree[before] = 0
#     queue = deque([i for i in adj if in_degree[i] == 0])
#     res = []
#     while queue:
#         current = queue.popleft()
#         res.append(current)
#         for neighbor in graph[current]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#     return res

# def get_total_number():
#     topo_order = get_topo_sorting()
#     topo_dict = {value: index for index, value in enumerate(reversed(topo_order))}
#     total = 0
#     _, page_numbers = parse_input()
#     for each in page_numbers:
#         number_list = [int(i) for i in each.split(",")]
#         if is_valid(number_list, topo_dict):
#             total += number_list[len(number_list) // 2]
#     return total

# def is_valid(number_list, topo_dict):
#     for i in range(1, len(number_list)):
#         if topo_dict[number_list[i]] > topo_dict[number_list[i - 1]]:
#             return False
#     return True

def brute_force_q1():
    res = 0
    dependency, page_numbers = parse_input()
    graph = defaultdict(set)
    for each in dependency:
        before, after = map(int, each.split('|'))
        if after not in graph[before]:
            graph[before].add(after)
    for page in page_numbers:
        l = page.split(",")
        l = [int(i) for i in l]
        if brute_force_valid(graph, l):
            res +=  l[len(l) // 2]
    return res

def brute_force_valid(graph, l):      
    for i in range(1, len(l)):
        if l[i] not in graph[l[i-1]]:
            return False
    return True

def brute_force_q2():
    res = 0
    dependency, page_numbers = parse_input()
    graph = defaultdict(set)
    for each in dependency:
        before, after = map(int, each.split('|'))
        if after not in graph[before]:
            graph[before].add(after)
    for page in page_numbers:
        l = page.split(",")
        l = [int(i) for i in l]
        flag, res_list = brute_force_valid_sort(graph, l)
        if not flag:
            res += res_list[len(res_list) // 2]
    return res

def brute_force_valid_sort(graph, l):
    flag = True
    res = l.copy()
    n = len(l)

    for i in range(n):
        for j in range(0, n - i - 1):
            if res[j+1] not in graph[res[j]]:
                flag = False
                res[j], res[j+1] = res[j+1], res[j]
    return flag, res  

def main():
    print(brute_force_q1())
    print(brute_force_q2())

if __name__ == "__main__":
    main()