from concurrent.futures import Future
from typing import Callable
from src.controller.executor import LockpickExecutor
from src.model.model_action import ModelAction


class Controller:

    def __init__(self, model: ModelAction) -> None:
        self.model = model
        self._executor = LockpickExecutor()

    def add_user(
        self, name: str, surname: str, username: str, password: str
    ) -> Future[None]:
        callable: Callable[[], None] = lambda: self.model.signup(
            name, surname, username, password
        )
        return self._executor.execute(callable)
