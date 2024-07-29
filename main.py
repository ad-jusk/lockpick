from os import environ

environ["KIVY_LOG_MODE"] = "MIXED"

from kivy.logger import Logger, LOG_LEVELS
from kivy.lang import Builder

from src.app import LockpickApp


def load_design_files() -> None:

    design_directory: str = "./src/design"
    Builder.load_file(design_directory + "/login.kv")
    Builder.load_file(design_directory + "/home.kv")


if __name__ == "__main__":

    # SET KIVY LOGGING LEVEL TO ERROR
    Logger.setLevel(LOG_LEVELS["error"])

    # LOAD DESIGN FILES
    load_design_files()

    # START APP
    LockpickApp().run()
