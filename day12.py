import util

def calculate_region_properties(grid):
    grid = [list(row) for row in grid.strip().split('\n')]
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    components = [[0] * cols for _ in range(rows)]

    areas = {}
    perimeters = {}
    corners = {}
    component_id = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, comp_id):
        stack = [(x, y)]
        visited[x][y] = True
        components[x][y] = comp_id
        area = 0
        perimeter = 0

        while stack:
            cx, cy = stack.pop()
            area += 1
            borders = 0

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if not is_valid(nx, ny) or grid[nx][ny] != grid[x][y]:
                    borders += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    components[nx][ny] = comp_id
                    stack.append((nx, ny))

            perimeter += borders

        return area, perimeter

    def count_corners():
        for x in range(rows):
            for y in range(cols):
                if visited[x][y]:
                    comp_id = components[x][y]
                    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        a = components[x][y]
                        b = components[x + dx][y] if is_valid(x + dx, y) else -1
                        c = components[x][y + dy] if is_valid(x, y + dy) else -1
                        d = components[x + dx][y + dy] if is_valid(x + dx, y + dy) else -1

                        if (a != b and a != c) or (a == b and a == c and a != d):
                            corners[comp_id] = corners.get(comp_id, 0) + 1
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                component_id += 1
                area, perimeter = dfs(i, j, component_id)
                areas[component_id] = area
                perimeters[component_id] = perimeter

    count_corners()

    part1 = sum(areas[comp_id] * perimeters[comp_id] for comp_id in areas)
    part2 = sum(areas[comp_id] * corners.get(comp_id, 0) for comp_id in areas)

    return part1, part2

map0 = """
AA
AA
"""
map1="""
AAAA
BBCD
BBCC
EEEC
"""

map2 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""

map3="""
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""

map4 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
input_map = util.get_input_data(12).strip()


print(f"Total Fence Price: {calculate_region_properties(input_map)}") #1465112, 893790
