import functools
from collections import defaultdict

class StoneSolver:
    @functools.lru_cache(maxsize=None)
    def transform_stone(self, stone):

        if stone == 0:
            return (1,)
        
        stone_str = str(stone)
        length = len(stone_str)
        if length % 2 == 0:
            return (
                int(stone_str[:length//2]), 
                int(stone_str[length//2:])
            )

        return (stone * 2024,)

    def solve(self, initial_stones, blinks):

        stone_counts = defaultdict(int)
        for stone in initial_stones:
            stone_counts[stone] += 1
        
        for _ in range(blinks):
            new_counts = defaultdict(int)
            
            for stone, count in stone_counts.items():
                transformed = self.transform_stone(stone)
                
                for new_stone in transformed:
                    new_counts[new_stone] += count
            
            stone_counts = new_counts
        return sum(stone_counts.values())

def main():
    solver = StoneSolver()
    
    puzzle_input = [572556,22,0,528, 4679021, 1, 10725, 2790]
    result = solver.solve(puzzle_input, 25)
    print(f"Number of stones after 25 blinks: {result}")
    result = solver.solve(puzzle_input, 75)
    print(f"Number of stones after 75 blinks: {result}")

if __name__ == "__main__":
    main()


