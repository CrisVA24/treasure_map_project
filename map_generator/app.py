from tkinter import Tk
from views.start_screen import StartScreen

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title('Treasure Trace')
        self.current_screen = StartScreen(self.root, self)

    def run(self):
        self.root.mainloop()
    '''
    def switch_screen(self, new_screen_class):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = new_screen_class(self.root, self)
    '''

