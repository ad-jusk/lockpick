from kivy.uix.screenmanager import Screen

from src.model.model_data import ModelData
from src.controller.controller import Controller
from src.view.utils.overlay import Overlay


class LoginScreen(Screen):

    def __init__(self, model: ModelData, controller: Controller, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.overlay = Overlay()
        self.add_widget(self.overlay)
