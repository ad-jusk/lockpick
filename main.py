from os import environ
import pathlib

environ["KIVY_LOG_MODE"] = "MIXED"

from kivy.logger import Logger, LOG_LEVELS
from kivy.lang import Builder

from src.app import LockpickApp


def load_design_files() -> None:
    for kv_file in pathlib.Path("./src/design").rglob("*.kv"):
        Builder.load_file(str(kv_file))


if __name__ == "__main__":

    # SET KIVY LOGGING LEVEL TO ERROR
    Logger.setLevel(LOG_LEVELS["error"])

    # LOAD DESIGN FILES
    load_design_files()

    # START APP
    LockpickApp().run()
