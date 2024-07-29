from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.view.login import LoginScreen
from src.view.home import HomeScreen
from src.model.model import Model
from src.controller.controller import Controller


class LockpickApp(App):

    def build(self) -> ScreenManager:

        model = Model()
        controller = Controller(model)

        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(model, controller, name="login"))
        screen_manager.add_widget(HomeScreen(model, controller, name="home"))

        return screen_manager
