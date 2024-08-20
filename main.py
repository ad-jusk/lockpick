from os import environ

environ["KIVY_LOG_MODE"] = "MIXED"

from kivy.logger import Logger, LOG_LEVELS
from kivy.lang import Builder

from src.app import LockpickApp


if __name__ == "__main__":

    # SET KIVY LOGGING LEVEL TO ERROR
    Logger.setLevel(LOG_LEVELS["error"])

    # START APP
    LockpickApp().run()
