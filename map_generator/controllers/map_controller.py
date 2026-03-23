class MapController:

    def __init__(self, model):
        self.model = model

    def handle_cell_click(self, x, y, tool):
        if tool == "obstacle":
            self.model.place_obstacle(x, y)
            return True, None

        elif tool == "treasure":
            self.model.place_treasure(x, y)
            return True, None

        elif tool == "start":
            success = self.model.set_start(x, y)

            if not success:
                return False, "Start point already placed."

            return True, "start_placed"
        
    def validate_map(self):
        if not self.model.has_start():
            return False, "Please set a starting point."

        if not self.model.has_treasures():
            return False, "Please add at least one treasure."

        return True, None

    def get_map_string(self):
        return self.model.to_string()
    
    def solve_map(self):
        valid, message = self.validate_map()

        if not valid:
            return False, message

        path = self.model.solve()

        if not path:
            return False, "No path found."

        return True, path