import curses
from curses import wrapper

class CursesAdapter:
    def __init__(self):
        self.x = 0
        self.y = 1
        self.key = None
        self.data_arr = []
        self.mod = False
        self.shift = 0
        self.k = 0
        self.k_buf = 0
    
    def get_char_wrapped(self, stdscr):
        try:
            self.key = stdscr.getkey()
            if self.key == "KEY_RESIZE":
                self.mod = False
        except:
            self.key = None

    def display_wrapped(self, stdscr, text_arr):
        stdscr.clear()
        stdscr.addstr(0, 30, f"STATUSBAR: Cur Mode = {self.data_arr[0]}; FileName = '{self.data_arr[1]}'; Line = {self.data_arr[2]}; LinesNum = {self.data_arr[3]}")
        if self.shift!=0:
            self.k = self.y//self.shift
        for i in range(len(text_arr)):
            try:
                stdscr.addstr(i+1, 0, text_arr[i+self.shift*self.k])
            except:
                if self.mod == False:
                    self.shift = i - 1
                    self.mod = True
                # pass
        #stdscr.addstr(5, 30, f"x = {self.x}; y = {self.y}, k = {self.k}. shift = {self.shift}")
        # stdscr.addstr(5, 30, f"keyy = {self.key}")
        try:
            stdscr.move(self.y - self.shift*self.k, self.x)
        except:
            pass
        stdscr.refresh()
    
    def get_command_wrapped(self,  stdscr, data_arr):
        stdscr.move(0, 30 + len(f"STATUSBAR: Cur Mode = {data_arr[0]}; FileName = '{data_arr[1]}'; Line = {data_arr[2]}; LinesNum = {data_arr[3]}"))

    def get_filename_wrapped(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 30, "Input filename: ")
        stdscr.move(0, 30+len("Input filename: "))
    
    def get_char(self):
        wrapper(self.get_char_wrapped)
    
    def display(self, text_arr):
        wrapper(self.display_wrapped, text_arr)
    
    def display_status(self, data_arr):
        self.data_arr = data_arr

    def get_command(self, data_arr):
        wrapper(self.get_command_wrapped, data_arr)
    
    def main_wrapped(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 30, self.filename)
        stdscr.addstr(4, 30, self.filename)
        stdscr.refresh()
        stdscr.getch()

