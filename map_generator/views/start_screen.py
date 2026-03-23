from tkinter import *

class StartScreen:

    def __init__(self, root, app):
        self.root = root
        self.app = app

        #Frame
        self.frame = Frame(self.root)
        self.frame.pack()


        #VARIABLES
        self.size_var = StringVar(value="")
        self.error_message_var = StringVar(value="")

        #TITLE
        self.title_label = Label(self.frame, text='Treasure Trace', fg='black', font=('Helvetica', 20, 'bold'))
        self.title_label.pack(pady=10)

        #MAIN CONTAINER
        self.main_container = Frame(self.frame)
        self.main_container.pack(pady=(0, 10))

        #INSTRUCTIONS
        self.instructions = Text(self.main_container, height=14, width=47, padx=20, pady=20)
        self.instructions.pack(side=LEFT, padx=10)
        self.instructions.insert(INSERT, "Welcome!\n\nUncover the secrets of ancient civilizations by\ndesigning your own mysterious maps. Place\nobstacles and hide treasures, then watch as\nour expert explorer reveals the quickest way to\nthe gold.\n\nSelect a map size from the options below to\nbuild your custom labyrinth with obstacles,\ntreasures, and a starting point. Once you save\nyour creation, the explorer will unlock and\nautomatically reveal the shortest path to the\nriches.")
        self.instructions.config(state=DISABLED)

        #SIZE BUTTONS CONTAINER
        self.button_container = Frame(self.main_container)
        self.button_container.pack(side=LEFT, padx=(0, 10))

        #SIZE BUTTONS
        options = ["Small", "Medium", "Large"]
        
        for item in options:
            button = Radiobutton(self.button_container,
                              text=item,
                              variable=self.size_var,
                              value=item,
                              indicatoron=0,
                              width=10,
                              font=('Helvetica', 12),
                              selectcolor="#d1d1d1",
                              bg='#ffffff')
            button.pack(pady=10)        

        #START BUTTON
        self.start_button = Button(self.frame, command=self.start, width=20, text='Start Adventure', font=('Helvetica', 18, 'bold'), bg='#ffffff',fg='black')
        self.start_button.pack(pady=(0, 10))

        #ERROR MESSAGE
        self.error_label = Label(self.frame, textvariable=self.error_message_var, fg="red")
        self.error_label.pack(pady=(0, 10))

    

    def start(self):
        from views.map_editor_screen import MapEditorScreen
        if self.size_var.get():
            self.app.switch_screen(MapEditorScreen, size=self.size_var.get())
        else:
            self.error_message_var.set("Please select a map size to continue")

    def destroy(self):
        self.frame.destroy()
