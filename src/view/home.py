from kivy.uix.screenmanager import Screen

from ..model.model_data import ModelData
from ..controller.controller import Controller

class HomeScreen(Screen):
    
    def __init__(self, model: ModelData, controller: Controller, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

    def test(self):
        self.controller.add_user("a", "b")