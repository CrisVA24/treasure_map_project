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
    
    #BACKTRACKING
    def solve(self):
        # Return empty path if no starting point is defined
        if not self.start:
            return []

        visited = set()

        def backtrack(x, y, path):
            # Out of bounds check
            if not (0 <= x < self.size and 0 <= y < self.size):
                return None

            # Skip if obstacle or already visited
            if self.grid[x][y] == '#' or (x, y) in visited:
                return None

            # Add current position to path and mark as visited
            path.append((x, y))
            visited.add((x, y))

            # If a treasure is found, return the path immediately
            if self.grid[x][y] == 'T':
                return path.copy()

            # Explore neighboring cells (down, up, right, left)
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                result = backtrack(x + dx, y + dy, path)
                if result:
                    return result

            # Backtrack: remove current position from path and visited set
            path.pop()
            visited.remove((x, y))

            return None

        # Start backtracking from the initial position
        result = backtrack(self.start[0], self.start[1], [])

        # Return the found path or an empty list if no solution exists
        return result if result else []
        
