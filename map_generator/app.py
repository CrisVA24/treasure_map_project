from tkinter import Tk
from views.start_screen import StartScreen
from views.map_editor_screen import MapEditorScreen

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title('Treasure Trace')
        self.current_screen = StartScreen(self.root, self)

    def run(self):
        self.root.mainloop()
    
    def switch_screen(self, screen_class):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = screen_class(self.root, self)
    

