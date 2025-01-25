from MyString import MyString as MyString
from abc import ABC, abstractmethod

class Observable(ABC):
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observer(self, arr):
        for observer in range(len(self.observers)):
            self.observers[observer].update(arr)

class MyTextModel(Observable):
    def __init__(self):
        super().__init__()

        self.state = 0
        self.x = 0
        self.y = 1        
        self.all_file = None
    
        self.text = None
        self.text_arr = []

        self.direction = -1
        self.copy_str = None
        self.f_cord = [0, 0]

    def do_up(self):
        if self.y - 1>0:
            self.y -= 1
        else:
            pass
    
    def do_down(self):
        if self.y -1 <len(self.text_arr):
            self.y += 1
        else:
            pass
    
    def do_left(self):
        self.x -=1
        if self.x<0:
            if self.y - 1>0:
                self.y -= 1
                self.x = len(self.text_arr[self.y - 1])
            else:
                self.x = 0
    
    def do_right(self):
        self.x +=1
        if self.x>len(self.text_arr[self.y - 1]):
            self.x = 0
            self.y += 1
            if self.y - 1==len(self.text_arr)-1:
                self.text_arr.append(" ")

    def erase(self):
        if self.x>0:
            self.text_arr[self.y - 1] = self.text_arr[self.y - 1][:self.x-1]+ self.text_arr[self.y - 1][self.x:]
        else:
            self.text_arr[self.y - 2] = self.text_arr[self.y - 2] + self.text_arr[self.y-1][self.x:]
            self.text_arr[self.y-1] = ""
        self.do_left()
    
    def add_char(self, key):
        try:
            self.text_arr[self.y-1] = self.text_arr[self.y-1][:self.x+1]+ key + self.text_arr[self.y-1][self.x+1:]
            self.x+=1
        except TypeError:
            pass
    
    def print_buf(self, n):
        if 1<=n and n<=len(self.text_arr):
            return self.text_arr[n-1].c_str()
        return ""
    
    def rewrite_buf(self):
        s2 = ""
        i=0
        
        s = self.all_file

        for c in s:
            s2+=c
                      
            if c == "\n":
                s2 = MyString(s2)
                self.text_arr.append(s2.c_str())
                s2 = ""
        s2+='\n'
        s2 = MyString(s2)
        self.text_arr.append(s2.c_str())

    def write_in_buf(self, filename):
        with open(filename) as f:
            s1=f.read()
        self.all_file = s1
        self.rewrite_buf()       

    def search_left(self, text):
        self.text = text
        self.direction = 0
        for i in range (self.y-1,-1,-1):
            if i==self.y-1:
                    t= self.text_arr[i][:self.x].rfind(self.text)
            else:
                    t= self.text_arr[i].rfind(self.text)
            if (t!=-1):
                    self.x = t
                    self.y = i+1
                    self.f_cord = [t, i+1]
                    self.state = 1
                    return
        self.f_cord = [self.x, self.y]
        return
    
    def search_right(self, text):
        self.text = text
        self.direction = 1
        for i in range(self.y-1,len(self.text_arr)):
            if i==self.y-1:
                    t = self.text_arr[i][self.x:].find(self.text)
            else:
                    t = self.text_arr[i].find(self.text)
            if t !=-1:
                    self.x = t
                    self.y = i+1
                    self.f_cord = [t, i+1]
                    self.state = 1
                    return
        self.f_cord = [self.x, self.y]
        return

    def do_command_null(self):
        self.x = 0
    
    def do_command_endline(self):
        self.x = len(self.text_arr[self.y-1])
    
    def do_command_gg(self):
        self.y = 1
        self.x = 0

    def do_command_G(self):
        self.y = len(self.text_arr)
        self.x = len(self.text_arr[-1]) - 1

    def do_command_NG(self, N):
        if len(self.text_arr) >= N  and N>=1:
            self.y = N
            self.x = 0
    
    def second_search_n(self):
        if self.direction==0:
            #self.search_left(self.text)
            self.direction = 0
            x = self.f_cord[0]
            y = self.f_cord[1]
            for i in range(y,-1,-1):
                if i==y-1:
                    t= self.text_arr[i][:x].rfind(self.text)
                else:
                    t= self.text_arr[i].rfind(self.text)
                if (t!=-1):
                    self.x = t
                    self.y = i+1
                    self.f_cord = [t, i+1]
                    self.state = 1
                    return
            self.f_cord = [self.x, self.y]
            return
        elif self.direction==1:
            # self.search_right(self.text)
            self.direction = 1
            x = self.f_cord[0]
            y = self.f_cord[1]
            for i in range(y,len(self.text_arr)):
                if i==y-1:
                    t = self.text_arr[i][x:].find(self.text)
                else:
                    t = self.text_arr[i].find(self.text)
                if t !=-1:
                    self.x = t
                    self.y = i+1
                    self.f_cord = [t, i+1]
                    self.state = 1
                    return
            self.f_cord = [self.x, self.y]
            return
        else:
            pass

    def second_search_N(self):
        if self.direction==1:
            #self.search_left(self.text)
            self.direction = 1
            x = self.f_cord[0]
            y = self.f_cord[1]
            for i in range(y,-1,-1):
                if i==y-1:
                    t= self.text_arr[i][:x-2].rfind(self.text)
                else:
                    t= self.text_arr[i].rfind(self.text)
                if (t!=-1):
                    self.x = t
                    self.y = i+1
                    self.f_cord = [t, i+1]
                    self.state = 1
                    return
            self.f_cord = [self.x, self.y]
            return
        elif self.direction==0:
            # self.search_right(self.text)
            self.direction = 0
            x = self.f_cord[0]
            y = self.f_cord[1]
            for i in range(y,len(self.text_arr)):
                if i==y-1:
                    t = self.text_arr[i][x:].find(self.text)
                else:
                    t = self.text_arr[i].find(self.text)
                if t !=-1:
                    self.x = t
                    self.y = i+1
                    self.f_cord = [t, i+1]
                    self.state = 1
                    return
            self.f_cord = [self.x, self.y]
            return
        else:
            pass
    
    def do_command_begin(self):
        self.y = 1            
        self.state = 1
        return
    
    def do_command_w(self, filename):
        f = open(filename, "w")
        s2 = '\n'.join(self.text_arr)
        s2 = MyString(s2)

        f.write(s2.c_str())
        f.close()

    def do_nav_w(self):
        self.x = self.text_arr[self.y-1][self.x:].find(' ') + self.x
        return

    def do_command_b(self):
        self.x = self.text_arr[self.y-1][:self.x].rfind(' ')    
        return

    def do_command_x(self):
        s = self.text_arr[self.y-1]
        s = s[:self.x-1] + s[self.x:]
        self.text_arr[self.y-1] = MyString(s).c_str()
        return
    
    def do_command_diw(self):
        s = self.text_arr[self.y-1]
        right = self.text_arr[self.y-1][self.x:].find(' ') + self.x
        left = self.text_arr[self.y-1][:self.x].rfind(' ')
        s = s[:left] + s[right:]
        self.text_arr[self.y-1] = MyString(s).c_str()
        return
    
    def do_command_dd(self):
        self.copy_str = self.text_arr[self.y-1]
        self.text_arr[self.y-1] = ""
        self.x = self.x-1
        self.y = 1

    def copy_return(self):
        return self.copy_str
    
    def do_command_yy(self):
        self.copy_str = self.text_arr[self.y-1]

    def do_command_yw(self):
        s = self.text_arr[self.y-1]
        right = 0
        if self.text_arr[self.y-1][self.x:].find(' ')!=-1:
            right = self.text_arr[self.y-1][self.x:].find(' ')
        else:
            right = self.text_arr[self.y-1][self.x:].find('\n') + self.x
        left = 0
        if self.text_arr[self.y-1][:self.x].rfind(' ') != -1:
            left = self.text_arr[self.y-1][:self.x].rfind(' ')+1
        else:
            left = self.text_arr[self.y-1][:self.x].rfind('\n')
        a = right
        a = a + self.x
        s = s[left:a]
        self.copy_str = s

    def do_command_p(self):
        if self.copy_str == None:
            pass
        else:
            if len(self.text_arr[self.y-1]) == 0:
                self.text_arr[self.y-1] = self.copy_str
            else:
                s = self.text_arr[self.y-1]
                copy = self.copy_str
                copy.replace("\n", " ")
                s1 = s[:self.x] + copy + s[self.x:]
                #s1 = MyString(s1)
                self.text_arr[self.y-1] = s1
                self.set_coordinates(self.x+len(copy), self.y)
                self.erase()
    
    def do_command_r(self):
        if self.copy_str == None:
            pass
        else:
            self.text_arr[self.y-1] = self.text_arr[self.y-1][:self.x]+ self.copy_str + self.text_arr[self.y-1][self.x+1:]
    
    def do_command_i(self, key):
        try:
            self.text_arr[self.y-1] = self.text_arr[self.y-1][:self.x-1]+ key + self.text_arr[self.y-1][self.x-1:]
            self.x+=1
        except TypeError:
            pass

    def set_coordinates(self, y, x):
        self.x = y
        self.y = x

    def return_coordinates(self):
        return [self.x, self.y]
    