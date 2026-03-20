from tkinter import *

class MapEditorScreen:

    def __init__(self, root, app, size):
        self.root = root
        self.app = app
        self.size = size

    def get_dimensions(self):
        sizes = {
            "Small": 15,
            "Medium": 20,
            "Large": 25
        }
        return sizes[self.size]

        #FRAME
        self.frame = Frame(self.root)
        self.frame.pack()

        #TITLE
        self.title_label = Label(self.frame, text='Treasure Trace', fg='black', font=('Helvetica', 20, 'bold'))
        self.title_label.pack(pady=10)