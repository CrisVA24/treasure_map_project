from tkinter import *
from models.map_model import MapModel
from controllers.map_controller import MapController


class MapEditorScreen:

    def __init__(self, root, app, size):
        self.root = root
        self.app = app

        #MAIN CONTAINER
        self.frame = Frame(self.root)
        self.frame.pack()

        #MODEL AND CONTROLLER
        self.size_map = self.get_dimensions(size)
        self.model = MapModel(self.size_map)
        self.controller = MapController(self.model)

        #VARIABLES
        self.selected_tool = StringVar(value="obstacle")

        #TITLE
        Label(
            self.frame,
            text="Treasure Trace",
            font=('Helvetica', 20, 'bold')
        ).pack(pady=10)

        #TOOLBAR
        toolbar = Frame(self.frame)
        toolbar.pack(pady=5)

        self.start_radio = Radiobutton(
            toolbar, text="Start (S)",
            variable=self.selected_tool,
            value="start",
            indicatoron=0,
            width=12
        )
        self.start_radio.grid(row=0, column=0, padx=5)

        Radiobutton(
            toolbar, text="Obstacle (#)",
            variable=self.selected_tool,
            value="obstacle",
            indicatoron=0,
            width=12
        ).grid(row=0, column=1, padx=5)

        Radiobutton(
            toolbar, text="Treasure (T)",
            variable=self.selected_tool,
            value="treasure",
            indicatoron=0,
            width=12
        ).grid(row=0, column=2, padx=5)

        #GRID
        self.grid_frame = Frame(self.frame)
        self.grid_frame.pack(pady=10)

        self.buttons = []
        self.create_grid()

        #MESSAGES
        self.message_var = StringVar(value="")
        Label(self.frame, textvariable=self.message_var, fg="red").pack()

        #BUTTONS
        Button(
            self.frame,
            text="Solve Map",
            command=self.solve_map_ui,
            width=20
        ).pack(pady=5)

        Button(
            self.frame,
            text="Clear Map",
            command=self.clear_map,
            width=20
        ).pack(pady=5)

        Button(
            self.frame,
            text="Back",
            command=self.go_back,
            width=20
        ).pack(pady=(5, 10))

    #GRID
    def create_grid(self):
        for i in range(self.size_map):
            row = []
            for j in range(self.size_map):

                btn = Button(
                    self.grid_frame,
                    text="",
                    width=2,
                    height=1,
                    font=('Consolas', 10),
                    command=lambda x=i, y=j: self.on_cell_click(x, y)
                )
                btn.grid(row=i, column=j)

                row.append(btn)

            self.buttons.append(row)

    #CLIC EVENT
    def on_cell_click(self, x, y):
        tool = self.selected_tool.get()

        success, message = self.controller.handle_cell_click(x, y, tool)

        if not success:
            self.message_var.set(message)
            return

        if message == "start_placed":
            self.start_radio.config(state=DISABLED)

        self.update_cell_ui(x, y)

    #UPDATE UI
    def update_cell_ui(self, x, y):
        value = self.model.grid[x][y]
        btn = self.buttons[x][y]

        btn.config(text=value)

    #SAVE MAPA
    def save_map(self):
        valid, message = self.controller.validate_map()

        if not valid:
            self.message_var.set(message)
            return

        try:
            with open("map.txt", "w") as file:
                file.write(self.controller.get_map_string())

            self.message_var.set("Map saved successfully!")

        except:
            self.message_var.set("Error saving the map.")

    #GET BACK
    def go_back(self):
        from views.start_screen import StartScreen
        self.app.switch_screen(StartScreen)

    # UTIL
    def get_dimensions(self, size_label):
        sizes = {
            "Small": 10,
            "Medium": 15,
            "Large": 20
        }
        return sizes[size_label]

    #DESTROY
    def destroy(self):
        self.frame.destroy()

    def solve_map_ui(self):
        # Validate the map before saving or solving
        valid, message = self.controller.validate_map()

        if not valid:
            self.message_var.set(message)
            return

        # Save the map to a file
        try:
            with open("map.txt", "w") as file:
                file.write(self.controller.get_map_string())
        except:
            self.message_var.set("Error saving the map.")
            return

        # Solve the map using backtracking
        success, result = self.controller.solve_map()

        if not success:
            self.message_var.set(result)

            # Create error file if no solution is found
            with open("mapa_err.txt", "w") as f:
                f.write(f"Error: map has no solution starting from coordinate {self.model.start}")

            return

        # Draw the path on the UI
        for (x, y) in result:
            if self.model.grid[x][y] == '.':
                self.buttons[x][y].config(text='*')

        # Display success message
        self.message_var.set("Map saved and path found!")

    def clear_map(self):
        # Reset the model and controller
        self.model = MapModel(self.size_map)
        self.controller = MapController(self.model)

        # Clear the UI grid
        for i in range(self.size_map):
            for j in range(self.size_map):
                self.buttons[i][j].config(text='')

        # Reset UI state
        self.selected_tool.set("obstacle")
        self.start_radio.config(state=NORMAL)
        self.message_var.set("")