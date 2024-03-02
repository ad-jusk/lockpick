from os import environ

environ["KIVY_LOG_MODE"] = "MIXED"

from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger, LOG_LEVELS

from logger import LOGGER

class LockpickApp(App):
    
    def build(self):
        return Builder.load_file("./design/main.kv")

if __name__ == "__main__":

    # SET KIVY LOGGING LEVEL TO ERROR
    Logger.setLevel(LOG_LEVELS['error'])

    LOGGER.info("Starting app...")

    LockpickApp().run()