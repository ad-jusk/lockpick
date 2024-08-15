from kivy.uix.screenmanager import Screen

from src.model.model_data import ModelData
from src.controller.controller import Controller


class StartScreen(Screen):

    def __init__(self, **kwargs: str) -> None:
        super().__init__(**kwargs)
