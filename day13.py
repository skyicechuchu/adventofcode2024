import re
import util


def parse_claw_machine_configs(input_text, mode="q1"):
    machines = []
    
    machine_texts = input_text.strip().split('\n\n')
    
    for machine_text in machine_texts:
        lines = machine_text.split('\n')
        
        a_match = re.search(r'Button A: X\+(\d+), Y\+(\d+)', lines[0])
        ax, ay = map(int, a_match.groups())
        
        b_match = re.search(r'Button B: X\+(\d+), Y\+(\d+)', lines[1])
        bx, by = map(int, b_match.groups())
        
        prize_match = re.search(r'Prize: X=(\d+), Y=(\d+)', lines[2])
        prize_x, prize_y = map(int, prize_match.groups())
        if mode == "q2":
            prize_x +=  10000000000000
            prize_y += 10000000000000
        machines.append({
            'ax': ax, 'ay': ay,
            'bx': bx, 'by': by,
            'prize_x': prize_x, 'prize_y': prize_y
        })
    
    return machines


def solve_claw_machines(input_text, mode="q1"):
    total = 0
    machines = parse_claw_machine_configs(input_text, mode)
    for machine in machines:
        ax, ay, bx, by, prize_x, prize_y = \
              machine['ax'], machine['ay'], machine['bx'], machine['by'], machine['prize_x'], machine['prize_y']
        m = (prize_x * by - prize_y * bx) // (ax * by - ay * bx)
        if m * (ax * by - ay * bx) != (prize_x * by - prize_y * bx):
            continue
        n = (prize_y - ay * m) // by
        if n * by != (prize_y - ay * m):
            continue
        total += 3 * m + n
    print(total)


input_text = util.get_input_data(13).strip()
solve_claw_machines(input_text,"q1")
solve_claw_machines(input_text,"q2")