from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from src.view.login import LoginScreen
from src.view.signup import SignupScreen
from src.view.start import StartScreen
from src.model.model import Model
from src.controller.controller import Controller

ASPECT_RATIO = 20 / 9
WINDOW_WIDTH = 300
WINDOW_HEIGHT = int(WINDOW_WIDTH * ASPECT_RATIO)

Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)


class LockpickApp(App):

    def build(self) -> ScreenManager:

        model = Model()
        controller = Controller(model)

        screen_manager = ScreenManager()
        screen_manager.add_widget(StartScreen(name="start"))
        screen_manager.add_widget(LoginScreen(model, controller, name="login"))
        screen_manager.add_widget(SignupScreen(model, controller, name="signup"))

        return screen_manager
