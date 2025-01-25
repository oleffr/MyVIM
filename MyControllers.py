class MyInputController:
    def __init__(self):
        self.adapter = None
        self.textmodel = None
        self.textview = None
        self.statusview = None
        self.filename = None
        self.state = False
    
    def do_input(self):
        while True:
            arr = {
                "text": self.textmodel.text_arr,
                "filename": self.filename,
                "y": self.adapter.y,
                "linenums": len(self.textmodel.text_arr)
            }

            self.textmodel.notify_observer(arr)
            self.statusview.view(self.adapter)
            self.textview.view(self.adapter)
            self.adapter.get_char()

            if self.adapter.key == "KEY_LEFT":
                self.textmodel.do_left()
            elif self.adapter.key=="KEY_RIGHT":
                self.textmodel.do_right()
            elif self.adapter.key=="KEY_UP":
                self.textmodel.do_up()
            elif self.adapter.key == "KEY_DOWN":
                self.textmodel.do_down()
            elif self.adapter.key == "KEY_F(8)": #############ENTER
                pass
            elif self.adapter.key == "KEY_F(9)": #############BACKSPACE
                self.textmodel.erase()
            elif self.adapter.key == "KEY_F(7)": #############РЕЖИМ КОМАНД ВВОДА
                self.get_command()
            elif self.adapter.key == ":":
                self.adapter.x = self.textmodel.x
                self.adapter.y = self.textmodel.y
                self.textview.text_arr = self.textmodel.text_arr
                break
            elif self.adapter.key == "KEY_RESIZE":
                pass
            elif self.adapter.key is not None:
                self.textmodel.add_char(self.adapter.key)
                self.state = True
            
            self.adapter.x = self.textmodel.x
            self.adapter.y = self.textmodel.y

            self.textview.text_arr = self.textmodel.text_arr

    def get_command(self):
        self.adapter.get_char()
        if self.adapter.key == "0":
            self.textmodel.do_command_null()
        elif self.adapter.key == "$":
            self.textmodel.do_command_endline()
        elif self.adapter.key == "w":
            self.textmodel.do_nav_w()
        elif self.adapter.key == "b":
            self.textmodel.do_command_b()
        elif self.adapter.key == "g":
            self.textmodel.do_command_gg()
        elif self.adapter.key == "G":
            self.textmodel.do_command_G()
            self.adapter.y = self.textmodel.y
            self.adapter.x = self.textmodel.x
            self.adapter.k = self.adapter.y//self.adapter.shift
            return
        elif self.adapter.key == "x":
            self.textmodel.do_command_x()
        elif self.adapter.key == "d":
            self.adapter.get_char()
            if self.adapter.key == "i":
                self.adapter.get_char()
                if self.adapter.key == "w":
                    self.textmodel.do_command_diw()
            elif self.adapter.key == "d":
                self.textmodel.do_command_dd()
        elif self.adapter.key == "y":
            self.adapter.get_char()
            if self.adapter.key == "y":
                self.textmodel.do_command_yy()
            elif self.adapter.key == "w":
                self.textmodel.do_command_yw()
        elif self.adapter.key == "p":
            self.textmodel.do_command_p()
        elif self.adapter.key == "I":
            self.textmodel.do_command_null()
        elif self.adapter.key == "A":
            self.textmodel.do_command_endline()
        elif self.adapter.key == "S":
            self.textmodel.do_command_dd()
            self.textmodel.do_command_null()
        elif self.adapter.key == "r":
            self.textmodel.do_command_r()
        elif self.adapter.key == "i":
            self.adapter.get_char()
            self.textmodel.do_command_i(self.adapter.key)
        elif self.adapter.key == "KEY_F(7)":
            self.adapter.k += 1
        elif self.adapter.key == "KEY_F(8)":
            if self.adapter.k>0:
                self.adapter.k -= 1
        elif self.adapter.key in "0123456789":
            str = self.adapter.key
            while True:
                self.adapter.get_char()
                if self.adapter.key in "0123456789":
                    str += self.adapter.key
                elif self.adapter.key == "G":
                    N = int(str)
                    self.textmodel.do_command_NG(N)
                    break
                else:
                    break

class MyCommandController:
    def __init__(self):
        self.adapter = None
        self.textmodel = None
        self.textview = None
        self.statusview = None
        self.filename = None
    
    def do_command(self):
        self.adapter.x = 0
        self.adapter.y = 1
        while True:
            arr = {
                "text": self.textmodel.text_arr,
                "filename": self.filename,
                "y": self.adapter.y,
                "linenums": len(self.textmodel.text_arr)
            }

            self.textmodel.notify_observer(arr)
            self.statusview.view(self.adapter)
            self.textview.view(self.adapter)
            self.adapter.get_char()

            if self.adapter.key == "KEY_LEFT":
                self.textmodel.do_left()
            elif self.adapter.key=="KEY_RIGHT":
                self.textmodel.do_right()
            elif self.adapter.key=="KEY_UP":
                pass
            elif self.adapter.key == "KEY_DOWN":
                pass
            elif self.adapter.key == "KEY_F(9)":
                self.textmodel.erase()
            elif self.adapter.key == "KEY_F(8)":
                self.adapter.x = self.textmodel.x
                self.adapter.y = self.textmodel.y
                self.textview.text_arr = self.textmodel.text_arr
                break
            elif self.adapter.key is not None:
                self.textmodel.add_char(self.adapter.key)
            
            self.adapter.x = self.textmodel.x
            self.adapter.y = self.textmodel.y

            self.textview.text_arr = self.textmodel.text_arr


class MyModeController:
    def __init__(self):
        self.input_controller = None
        self.command_controller = None
        self.text_model = None
        self.text_view = None
        self.adapter = None
        self.status_view = None
        self.buf = []
        self.buf_x = None
        self.buf_y = None

    def start(self):
        text = """hello11234455677
hi
my world
lovely world
world"""
        self.text_model.text_arr = text.split("\n")
        self.text_view.text_arr = text.split("\n")

        self.status_view.mode = "Input"
        self.status_view.filename = "No file"
        self.status_view.linenum = self.adapter.y
        self.status_view.linenums = len(self.text_model.text_arr)

        self.input_controller.adapter = self.adapter
        self.input_controller.textmodel = self.text_model
        self.input_controller.textview = self.text_view
        self.input_controller.statusview = self.status_view

        self.text_model.add_observer(self.text_view)
        self.text_model.add_observer(self.status_view)

        self.input_controller.do_input()

        if self.adapter.key == ":":
            self.choose_command()
    
    def choose_command(self):
        self.buf = self.text_model.text_arr
        self.buf_x = self.text_model.x
        self.buf_y = self.text_model.y
        text = ""
        self.text_model.text_arr = text.split("\n")
        self.text_view.text_arr = text.split("\n")

        self.status_view.mode = "Command"
        self.status_view.filename = "No file"
        self.status_view.linenum = self.adapter.y
        self.status_view.linenums = len(self.text_model.text_arr)

        self.command_controller.adapter = self.adapter
        self.command_controller.textmodel = self.text_model
        self.command_controller.textview = self.text_view
        self.command_controller.statusview = self.status_view

        self.adapter.x = 0
        self.text_model.x = 0
        self.text_model.y = 1
        self.adapter.k_buf = self.adapter.k

        self.command_controller.do_command()

        self.status_view.mode = "Input"
        if self.text_model.text_arr[0][0] == "o":
            buf = self.text_model.text_arr
            self.text_model.text_arr = []
            self.text_model.write_in_buf(buf[0][2:])
            self.input_controller.filename = buf[0][2:]
            self.command_controller.filename = buf[0][2:]
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0] == "wq!":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.x = self.buf_x
            self.text_model.do_command_w(self.command_controller.filename)
            self.adapter.key = None
            exit()
        elif self.text_model.text_arr[0] == "q!":
            exit()
        elif self.text_model.text_arr[0] == "q":
            if self.input_controller.state == False:
                exit()
            else:
                pass
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "w":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.x = self.buf_x
            if len(buf)>2:
                self.text_model.do_command_w(buf[0][2:])
            else:
                self.text_model.do_command_w(self.command_controller.filename)
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "x":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.x = self.buf_x
            if len(buf)>2:
                self.text_model.do_command_w(buf[0][2:])
            else:
                self.text_model.do_command_w(self.command_controller.filename)
            self.adapter.key = None
            exit()
        elif self.text_model.text_arr[0][0] in "123456789":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.x = 0
            self.adapter.y = int(buf[0])
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "h":
            self.text_model.x = 0

            self.text_model.text_arr = [
                'COMMAND HELPER:',
                '0 - curses to the start of the line',
                '$ - curses to the end of the line',
                'dd - cut line',
                'yy - copy line'
            ]

            arr = {
                "text": self.text_model.text_arr,
                "filename": self.command_controller.filename,
                "y": self.adapter.y,
                "linenums": len(self.text_model.text_arr)
            }

            self.text_model.notify_observer(arr)
            self.status_view.view(self.adapter)
            self.text_view.view(self.adapter)
            self.adapter.get_char()

            self.text_model.text_arr = self.buf
            self.text_model.x = self.buf_x

            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "/":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.search_right(buf[0][1:])
            self.adapter.x = self.text_model.f_cord[0]
            self.adapter.y = self.text_model.f_cord[1]
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "?":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.search_left(buf[0][1:])
            self.adapter.x = self.text_model.f_cord[0]
            self.adapter.y = self.text_model.f_cord[1]
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "n":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.second_search_n()
            self.adapter.x = self.text_model.f_cord[0]
            self.adapter.y = self.text_model.f_cord[1]
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        elif self.text_model.text_arr[0][0] == "N":
            buf = self.text_model.text_arr
            self.text_model.text_arr = self.buf
            self.text_model.second_search_N()
            self.adapter.x = self.text_model.f_cord[0]
            self.adapter.y = self.text_model.f_cord[1]
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
        else:
            self.text_model.text_arr = self.buf
            self.adapter.key = None
            self.input_controller.do_input()
            if self.adapter.key == ":":
                self.choose_command()
