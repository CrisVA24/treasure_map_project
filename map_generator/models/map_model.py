class MapModel:

    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.start = None
        self.treasures = []

    def place_obstacle(self, x, y):
        self.grid[x][y] = '#'

    def place_treasure(self, x, y):
        self.grid[x][y] = 'T'
        self.treasures.append((x, y))

    def set_start(self, x, y):
        if self.start is not None:
            return False
        
        self.grid[x][y] = 'S'
        self.start = (x, y)
        return True
    
    def clear_cell(self, x, y):
        self.grid[x][y] = '.'

    def has_start(self):
        return self.start is not None
    
    def has_treasures(self):
        return len(self.treasures) > 0
    
    def to_string(self):
        return '\n'.join(''.join(row) for row in self.grid)
        
