from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp

from enum import Enum

from src.view.utils.loading import LoadingIcon


class ToastLevel(Enum):
    INFO: tuple = (0.12, 0.57, 0.31, 1)
    WARN: tuple = (0.75, 0.75, 0.1, 1)
    ERROR: tuple = (0.85, 0.21, 0.21, 1)


class ToastLabel(Label):

    def __init__(self, bg_color: tuple, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = dp(40)
        self.padding = (dp(10), dp(10))
        self.font_size = dp(16)

        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[dp(10)])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args: str) -> None:
        self.rect.size = self.size
        self.rect.pos = self.pos


class Overlay(FloatLayout):

    def __init__(self, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.toast_container = BoxLayout(
            orientation="vertical",
            size_hint=(0.8, None),
            height=0,
            spacing=dp(10),
            pos_hint={"top": 1, "center_x": 0.5},
        )
        self.add_widget(self.toast_container)

    def add_toast(self, message: str, level: ToastLevel, duration: float = 2) -> None:
        toast = ToastLabel(level.value, text=message)
        self.toast_container.add_widget(toast)
        self.toast_container.height += toast.height + self.toast_container.spacing

        anim = Animation(opacity=1, duration=0.5)
        anim.start(toast)

        Clock.schedule_once(lambda dt: self.__remove_toast(toast), duration)

    def __remove_toast(self, toast: ToastLabel) -> None:
        anim = Animation(opacity=0, duration=0.5)
        anim.bind(on_complete=lambda *args: self.__finish_removal(toast))
        anim.start(toast)

    def __finish_removal(self, toast: ToastLabel) -> None:
        self.toast_container.remove_widget(toast)
        self.toast_container.height -= toast.height + self.toast_container.spacing

    def start_loading(self) -> None:
        if "loading" in self.ids:
            return
        loading = LoadingIcon()
        self.ids["loading"] = loading
        self.add_widget(loading)
        if self.parent:
            self.parent.disabled = True

    def stop_loading(self) -> None:
        self.remove_widget(self.ids["loading"])
        if self.parent:
            self.parent.disabled = False
