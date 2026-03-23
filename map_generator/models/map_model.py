class MapModel:

    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.start = None
        self.treasures = []

    def place_obstacle(self, x, y):
        if self.grid[x][y] in ['S', 'T']:
            return
        self.grid[x][y] = '#'

    def place_treasure(self, x, y):
        if self.grid[x][y] in ['S', '#']:
            return

        self.grid[x][y] = 'T'

        if (x, y) not in self.treasures:
            self.treasures.append((x, y))

    def set_start(self, x, y):
        if self.start is not None:
            return False

        self.start = (x, y)
        self.grid[x][y] = 'S'
        return True
    
    def clear_cell(self, x, y):
        self.grid[x][y] = '.'

    def has_start(self):
        return self.start is not None
    
    def has_treasures(self):
        return len(self.treasures) > 0
    
    def to_string(self):
        return '\n'.join(''.join(row) for row in self.grid)
    
    # Backtracking

    def solve(self):
        if not self.start:
            return []

        start = self.start
        visited = set()

        best_path = []
        best_length = float('inf')

        def backtrack(x, y, path):
            nonlocal best_path, best_length

            if not (0 <= x < self.size and 0 <= y < self.size):
                return

            if self.grid[x][y] == '#' or (x, y) in visited:
                return

            path.append((x, y))
            visited.add((x, y))

            if self.grid[x][y] == 'T':
                if len(path) < best_length:
                    best_path = path.copy()
                    best_length = len(path)
            else:
                backtrack(x+1, y, path)
                backtrack(x-1, y, path)
                backtrack(x, y+1, path)
                backtrack(x, y-1, path)

            path.pop()
            visited.remove((x, y))

        backtrack(start[0], start[1], [])

        return best_path
        
