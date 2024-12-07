import util
import collections
from itertools import product

def parse_data():
    puzzle_input = util.get_input_data(7)
    data_set = collections.defaultdict(list)
    for line in puzzle_input.split("\n"):
        temp = []
        for i in line.split(":")[1].split(" "):
            if len(i) == 0:
                continue
            data_set[int(line.split(":")[0])].append(int(i))
    return data_set

def get_total_value_q1():
    data_set = parse_data()
    res = 0
    for k, v in data_set.items():
        if permutation_check_two_sign(target=k, values=v):
            res += k
    return res

def get_total_value_q2():
    data_set = parse_data()
    res = 0
    for k, v in data_set.items():
        if permutation_check_three_sign(target=k, values=v):
            res += k
    return res

def permutation_check_two_sign(target, values):
    def evaluate(ops):
        expr = values.copy()
        for i in range(len(ops)):
            if ops[i] == '+':
                expr[i+1] = expr[i] + expr[i+1]
            else: 
                expr[i+1] = expr[i] * expr[i+1]
        return expr[-1]
    
    for ops in product(['+', '*'], repeat=len(values)-1):
        result = evaluate(ops)
        if result == target:
            return True
    
    return False

def permutation_check_three_sign(target, values):
    def evaluate(ops):
        expr = values.copy()
        for i in range(len(ops)):
            if ops[i] == '+':
                expr[i+1] = expr[i] + expr[i+1]
            elif ops[i] == '*': 
                expr[i+1] = expr[i] * expr[i+1]
            else:
                expr[i+1] = int(str(expr[i]) + str(expr[i+1]))
        return expr[-1]
    
    for ops in product(['+', '*', "||"], repeat=len(values)-1):
        result = evaluate(ops)
        if result == target:
            return True
    
    return False


print(get_total_value_q1())

print(get_total_value_q2())