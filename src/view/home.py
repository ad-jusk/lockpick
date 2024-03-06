from kivy.uix.screenmanager import Screen
from controller.controller import Controller

class HomeScreen(Screen):
    
    def __init__(self, controller: Controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def test(self):
        self.controller.test()