from tkinter import Tk
from views.start_screen import StartScreen

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title('Treasure Trace')
        self.root.geometry('500x405')
        self.current_screen = StartScreen(self.root)

    def run(self):
        self.root.mainloop()

