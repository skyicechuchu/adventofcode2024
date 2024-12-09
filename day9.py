import util

def generate_blocks(nums):
    res = []
    c = 0
    for i in range(1, len(nums)+1, 2):
        res.extend([c] * int(nums[i-1]))
        if i == len(nums):
            continue
        
        res.extend(["."] * int(nums[i]))
        c += 1
    return res

def q1(nums):
    res = generate_blocks(nums)
    i = 0
    j = len(res) - 1

    while i < j:
        if res[i] != ".":
            i += 1
        elif res[j] == ".":
            j -= 1
        else:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
    total = 0
    for i , val in enumerate(res):
        if val == ".":
            break
        total += val * i
    print(total)

def q2(nums):
    res = generate_blocks(nums)
    blocks = res.copy()
    files = {}
    for i, block in enumerate(blocks):
        if isinstance(block, int):
            if block not in files:
                files[block] = {'start': i, 'size': 0}
            files[block]['size'] += 1
    
    for file_num in sorted(files.keys(), reverse=True):
        file_info = files[file_num]
        current_start = file_info['start']
        file_size = file_info['size']
        
        best_move = None
        for start in range(current_start):
            if all(blocks[start+i] == '.' for i in range(file_size)):
                best_move = start
                break
        
        if best_move is not None:
            for i in range(current_start, current_start + file_size):
                blocks[i] = '.'
            
            for i in range(file_size):
                blocks[best_move + i] = file_num
    print(blocks)
    total = 0
    for i , val in enumerate(blocks):
        if val == ".":
            continue
        total += val * i
    print(total)


parse_data = util.get_input_data(9).strip()
q1(parse_data)
q2(parse_data)