from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, arr):
        pass

class MyTextView(Observer):
    def __init__(self):
        self.text_arr = None
    
    def view(self, adapter):
        adapter.display(self.text_arr)
    
    def update(self, arr):
        self.text_arr = arr["text"]

class MyStatusView(Observer):
    def __init__(self):
        self.mode = None
        self.filename = None
        self.linenum = None
        self.linenums = None
        self.data_arr = None
    
    def view(self, adapter):
        adapter.display_status(self.data_arr)
    
    def update(self, arr):
        self.filename = arr["filename"]
        self.linenum = arr["y"]
        self.linenums = arr["linenums"]
        self.data_arr = [self.mode, self.filename, self.linenum, self.linenums]

    