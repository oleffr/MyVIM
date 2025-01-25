from abc import ABC, abstractmethod
from MyAdapter import CursesAdapter
from MyView import MyStatusView
from MyTextModel import MyTextModel
from MyView import MyTextView
from MyControllers import MyCommandController, MyModeController, MyInputController

class DirectorMVC:

    def __init__(self):
        self.builder = None
    
    def set_builder(self, builder):
        self.builder = builder
    
    def build_MVC(self, class_arr):
        self.builder.set_controllers(class_arr["controllers"])
        self.builder.set_models(class_arr["controllers"]["mode"],class_arr["models"])
        self.builder.set_views(class_arr["controllers"]["mode"], class_arr["views"])
    
    def start(self, class_arr):
        self.builder.start(class_arr)


class Builder(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def set_controllers(self, class_arr):
        pass
    
    @abstractmethod
    def set_models(self, class_arr):
        pass

    @abstractmethod
    def set_views(self, class_arr):
        pass
    

class BuilderVIM(Builder):

    def start(self, class_arr):
        class_arr["controllers"]["mode"].start()

    def set_controllers(self, class_arr):
        mode_controller = class_arr["mode"]
        input_controller = class_arr["input"]
        command_controller = class_arr["command"]
        adapter = class_arr["adapter"]
        mode_controller.input_controller = input_controller
        mode_controller.command_controller = command_controller
        mode_controller.adapter = adapter

    def set_models(self, mode_controller, class_arr):
        mode_controller.text_model = class_arr["text"]

    def set_views(self, mode_controller, class_arr):
        mode_controller.text_view = class_arr["text"]
        mode_controller.status_view = class_arr["status"]


if __name__=="__main__":
    vim_director = DirectorMVC()
    vim_director.set_builder(BuilderVIM())
    class_arr = {
        "controllers": {"mode": MyModeController(), "input": MyInputController(), "command": MyCommandController(), "adapter": CursesAdapter()},
        "models": {"text": MyTextModel()},
        "views": {"text": MyTextView(), "status": MyStatusView()}
    }
    vim_director.build_MVC(class_arr)
    vim_director.start(class_arr)
