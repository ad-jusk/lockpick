from kivy.uix.screenmanager import ScreenManager, NoTransition

from src.controller.controller import Controller
from src.model.model import Model
from src.view.login import LoginScreen
from src.view.signup import SignupScreen
from src.view.start import StartScreen


class LockpickScreenManager(ScreenManager):

    def __init__(self, model: Model, controller: Controller, **kwargs: str):
        super().__init__(**kwargs)

        self.transition = NoTransition()

        self.add_widget(StartScreen(name="start"))
        self.add_widget(LoginScreen(model, controller, name="login"))
        self.add_widget(SignupScreen(model, controller, name="signup"))
