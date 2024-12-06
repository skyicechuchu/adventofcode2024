import util

"""
Q1: O(m+n) 2D graph handel
Q2: ugly brute force. O(n^2), scan all elements and treat as block. Need find O(n) on redit
"""

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class GuardPathFinder:
    def __init__(self, map_input):
        self.map = [list(row) for row in map_input.split('\n') if row.strip()]
        self.rows, self.cols = len(self.map), len(self.map[0])
        self.x, self.y, self.direction = self._find_initial_position()
        self.visited = set()

    def _find_initial_position(self):
        for r, row in enumerate(self.map):
            for c, cell in enumerate(row):
                if cell == '^':  
                    return r, c, 0  

    def _move_guard(self):
        self.visited.add((self.x, self.y))
        while True:
            dx, dy = DIRECTIONS[self.direction]
            nx, ny = self.x + dx, self.y + dy
            if not (0 <= nx < self.rows and 0 <= ny < self.cols):
                break
            if self.map[nx][ny] == "#":  
                self.direction = (self.direction + 1) % 4
            else:
                self.x, self.y = nx, ny
                self.visited.add((self.x, self.y))

    def solve_q1(self):
        self._move_guard()
        return len(self.visited)

    def solve_q2(self):
        return sum(
            1 for r in range(self.rows) for c in range(self.cols)
            if self.map[r][c] != "#" and (r, c) != (self.x, self.y) and self._is_blocked(r, c)
        )

    def _is_blocked(self, target_x, target_y):
        guard_row, guard_col, guard_dir = self.x, self.y, self.direction
        seen_states = {(guard_row, guard_col, guard_dir)}

        while True:
            dr, dc = DIRECTIONS[guard_dir]
            nr, nc = guard_row + dr, guard_col + dc
            if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                return False

            next_cell = "#" if (nr, nc) == (target_x, target_y) else self.map[nr][nc]
            if next_cell == "#":
                guard_dir = (guard_dir + 1) % 4 
            else:
                guard_row, guard_col = nr, nc

            if (guard_row, guard_col, guard_dir) in seen_states:
                return True
            seen_states.add((guard_row, guard_col, guard_dir))


def solve_guard_path_q1(map_input):
    return GuardPathFinder(map_input).solve_q1()


def solve_guard_path_q2(map_input):
    return GuardPathFinder(map_input).solve_q2()

map_data = util.get_input_data(6)
print(f"Distinct positions visited: {solve_guard_path_q1(map_data)}")  # Expected: 5153
print(f"Obstruction count: {solve_guard_path_q2(map_data)}")  # Expected: 1711
