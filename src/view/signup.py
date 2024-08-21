from kivy.uix.screenmanager import Screen

from src.model.model_data import ModelData
from src.controller.controller import Controller
from src.view.utils.toast import ToastLevel, ToastNotification


class SignupScreen(Screen):

    def __init__(self, model: ModelData, controller: Controller, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.toast = ToastNotification()
        self.add_widget(self.toast)

    def add_toast(self) -> None:
        self.toast.add_toast("Signup successful", ToastLevel.INFO)
