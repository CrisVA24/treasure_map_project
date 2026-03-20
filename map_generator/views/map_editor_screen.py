from tkinter import *

class MapEditorScreen:

    def __init__(self, root, app):
        self.root = root
        self.app = app

        #FRAME
        self.frame = Frame(self.root)
        self.frame.pack()

        #TITLE
        self.title_label = Label(self.frame, text='Treasure Trace', fg='black', font=('Helvetica', 20, 'bold'))
        self.title_label.pack(pady=10)