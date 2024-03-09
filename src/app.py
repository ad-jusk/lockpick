from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from .view.login import LoginScreen
from .view.home import HomeScreen
from .model.model import Model
from .controller.controller import Controller

class LockpickApp(App):
    
    def build(self) -> ScreenManager:

        model = Model()
        controller = Controller(model)

        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(model, controller, name = 'login'))
        screen_manager.add_widget(HomeScreen(model, controller, name = 'home'))

        return screen_manager