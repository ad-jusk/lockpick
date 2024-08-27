from kivy.app import App
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from src.screens import LockpickScreenManager
from src.model.model import Model
from src.controller.controller import Controller

import pathlib


def set_window_size() -> None:
    if platform != "android":
        ASPECT_RATIO = 20 / 9
        WINDOW_WIDTH = 300
        WINDOW_HEIGHT = int(WINDOW_WIDTH * ASPECT_RATIO)
        Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)


def load_design_files() -> None:
    for kv_file in pathlib.Path("./src/design").rglob("*.kv"):
        Builder.load_file(str(kv_file))


class LockpickApp(App):

    set_window_size()

    load_design_files()

    def build(self) -> ScreenManager:

        model = Model()
        controller = Controller(model)
        screen_manager = LockpickScreenManager(model, controller)

        return screen_manager
