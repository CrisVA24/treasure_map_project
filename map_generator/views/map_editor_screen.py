from tkinter import *
from models.map_model import MapModel
from controllers.map_controller import MapController


class MapEditorScreen:

    def __init__(self, root, app, size):
        self.root = root
        self.app = app

        # CONTENEDOR
        self.frame = Frame(self.root)
        self.frame.pack()

        # MODELO + CONTROLLER
        self.size_map = self.get_dimensions(size)
        self.model = MapModel(self.size_map)
        self.controller = MapController(self.model)

        # VARIABLES
        self.selected_tool = StringVar(value="obstacle")

        # TITLE
        Label(self.frame, text="Treasure Trace",
              font=('Helvetica', 20, 'bold')).pack(pady=10)

        # TOOLBAR
        toolbar = Frame(self.frame)
        toolbar.pack(pady=5)

        self.start_radio = Radiobutton(
            toolbar, text="Start", variable=self.selected_tool,
            value="start", indicatoron=0, width=10
        )
        self.start_radio.grid(row=0, column=0)

        Radiobutton(toolbar, text="Obstacle", variable=self.selected_tool,
                    value="obstacle", indicatoron=0, width=10).grid(row=0, column=1)

        Radiobutton(toolbar, text="Treasure", variable=self.selected_tool,
                    value="treasure", indicatoron=0, width=10).grid(row=0, column=2)

        # GRID
        self.grid_frame = Frame(self.frame)
        self.grid_frame.pack(pady=10)

        self.buttons = []
        self.create_grid()

        # ERROR LABEL
        self.error_message_var = StringVar(value="")
        Label(self.frame, textvariable=self.error_message_var, fg="red").pack()

        # SAVE BUTTON
        Button(self.frame, text="Save Map",
               command=self.save_map).pack(pady=5)

        # BACK BUTTON
        Button(self.frame, text="Back",
               command=self.go_back).pack(pady=5)

    # -------------------------
    # GRID
    # -------------------------

    def create_grid(self):
        for i in range(self.size_map):
            row = []
            for j in range(self.size_map):
                btn = Button(
                    self.grid_frame,
                    width=2,
                    height=1,
                    bg="white",
                    command=lambda x=i, y=j: self.on_cell_click(x, y)
                )
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    # -------------------------
    # EVENTO CLICK
    # -------------------------

    def on_cell_click(self, x, y):
        tool = self.selected_tool.get()

        success, message = self.controller.handle_cell_click(x, y, tool)

        if not success:
            self.error_message_var.set(message)
            return

        if message == "start_placed":
            self.start_radio.config(state=DISABLED)

        self.update_cell_ui(x, y)

    # -------------------------
    # UI UPDATE
    # -------------------------

    def update_cell_ui(self, x, y):
        value = self.model.grid[x][y]
        btn = self.buttons[x][y]

        colors = {
            '#': "gray",
            'T': "gold",
            'S': "green",
            '.': "white"
        }

        btn.config(bg=colors.get(value, "white"))

    # -------------------------
    # SAVE
    # -------------------------

    def save_map(self):
        valid, message = self.controller.validate_map()

        if not valid:
            self.error_message_var.set(message)
            return

        try:
            with open("map.txt", "w") as file:
                file.write(self.controller.get_map_string())

            self.error_message_var.set("Map saved successfully!")

        except:
            self.error_message_var.set("Error saving the map.")

    # -------------------------
    # NAVIGATION
    # -------------------------

    def go_back(self):
        from views.start_screen import StartScreen
        self.app.switch_screen(StartScreen)

    # -------------------------
    # UTIL
    # -------------------------

    def get_dimensions(self, size_label):
        sizes = {"Small": 15, "Medium": 20, "Large": 25}
        return sizes[size_label]

    # -------------------------
    # DESTROY
    # -------------------------

    def destroy(self):
        self.frame.destroy()