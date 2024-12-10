import util
def find_trails(topo_map):
    rows, cols = len(topo_map), len(topo_map[0])
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def can_move(x1, y1, x2, y2):
        if topo_map[x1][y1] == "." or topo_map[x2][y2] == ".":
            return False
        return (
            is_valid(x2, y2) and 
            (int(topo_map[x2][y2]) - int(topo_map[x1][y1])) == 1
        )
    
    
    def dfs(start_x, start_y, visited=None, peak_set=None):
        if visited is None:
            visited = set([(start_x, start_y)])
        if peak_set is None:
            peak_set = set()
        if int(topo_map[start_x][start_y]) == 9:
            peak_set.add((start_x, start_y))

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in moves:
            next_x, next_y = start_x + dx, start_y + dy
            
            if (is_valid(next_x, next_y) and 
                can_move(start_x, start_y, next_x, next_y) and 
                (next_x, next_y) not in visited):
                new_visited = visited.copy()
                new_visited.add((next_x, next_y))
                
                dfs(next_x, next_y, new_visited, peak_set)
        return peak_set
    
    
    res = []
    for x in range(rows):
        for y in range(cols):
            if topo_map[x][y] == '0':
                peaks = dfs(x, y)
                res.append(len(peaks))
    
    
    return res

def find_trail_ratings(topo_map):
    rows, cols = len(topo_map), len(topo_map[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def can_move(x1, y1, x2, y2):
        if topo_map[x1][y1] == "." or topo_map[x2][y2] == ".":
            return False
        return (
            is_valid(x2, y2) and 
            (int(topo_map[x2][y2]) - int(topo_map[x1][y1])) == 1
        )
    
    def count_trails(start_x, start_y):
        memo = {}

        def dfs(x, y, height):
            if (x, y, height) in memo:
                return memo[(x, y, height)]
                        
            if height == 9:
                return 1
            
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            total_trails = 0
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy

                if is_valid(next_x, next_y) and can_move(x, y, next_x, next_y):
                    total_trails += dfs(next_x, next_y, int(topo_map[next_x][next_y]))
        
            memo[(x, y, height)] = total_trails
            return total_trails
        
        return dfs(start_x, start_y, int(topo_map[start_x][start_y]))
    
    trailhead_ratings = []
    for x in range(rows):
        for y in range(cols):
            if topo_map[x][y] == '0':
                trailhead_ratings.append(count_trails(x, y))
    return trailhead_ratings

def solve_q1(input_map):
    return sum(find_trails(input_map.split('\n')))

def solve_q2(input_map):
    return sum(find_trail_ratings(input_map.split('\n')))


example1 = util.get_input_data(10)
print(solve_q1(example1)) 
print(solve_q2(example1)) 
