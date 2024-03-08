from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from view.login import LoginScreen
from view.home import HomeScreen
from controller.controller import Controller

class LockpickApp(App):

    def _load_design_files(self) -> None:

        design_directory: str = './design'
        Builder.load_file(design_directory + "/login.kv")
        Builder.load_file(design_directory + "/home.kv")
    
    def build(self) -> ScreenManager:

        self._load_design_files()

        controller = Controller()

        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(controller, name = 'login'))
        screen_manager.add_widget(HomeScreen(controller, name = 'home'))

        return screen_manager