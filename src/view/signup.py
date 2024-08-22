from kivy.uix.screenmanager import Screen

from src.model.model_data import ModelData
from src.controller.controller import Controller
from src.view.utils.toast import ToastNotification


class SignupScreen(Screen):

    def __init__(self, model: ModelData, controller: Controller, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.toast = ToastNotification()
        self.add_widget(self.toast)

    def signup(self) -> None:
        task = self.controller.add_user("JOHN", "DOE", "US", "PASS")
