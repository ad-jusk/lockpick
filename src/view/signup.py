from concurrent.futures import Future
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from log.logger import LOGGER
from src.model.model_data import ModelData
from src.controller.controller import Controller
from src.view.utils.toast import ToastLevel, ToastNotification


class SignupScreen(Screen):

    name_input: TextInput = ObjectProperty(None)
    surname_input: TextInput = ObjectProperty(None)
    username_input: TextInput = ObjectProperty(None)
    password_input: TextInput = ObjectProperty(None)

    def __init__(self, model: ModelData, controller: Controller, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.toast = ToastNotification()
        self.add_widget(self.toast)

    def signup(self) -> None:
        name: str = self.name_input.text
        surname: str = self.surname_input.text
        username: str = self.username_input.text
        password: str = self.password_input.text

        try:
            if not name or not surname or not username or not password:
                raise RuntimeError("Please fill account data")
            task = self.controller.signup(name, surname, username, password)
            task.add_done_callback(self.on_signup_complete)
        except RuntimeError as e:
            self.toast.add_toast(str(e), ToastLevel.ERROR)

    def on_signup_complete(self, signup_task: Future[None]) -> None:
        try:
            signup_task.result()
        except Exception as e:
            LOGGER.exception(e)
            self.toast.add_toast("Failed to create an account", ToastLevel.ERROR)
