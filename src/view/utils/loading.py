from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.properties import NumericProperty


class LoadingIcon(Image):

    angle = NumericProperty(0)

    def __init__(self, **kwargs: str) -> None:
        super(LoadingIcon, self).__init__(**kwargs)
        anim = Animation(angle=360, duration=2)
        anim += Animation(angle=360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item: Image, angle: int) -> None:
        if angle == 360:
            item.angle = 0
