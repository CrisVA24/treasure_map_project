

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

    
        
