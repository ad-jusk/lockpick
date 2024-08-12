from src.model.entity.user import User
from src.model.model_action import ModelAction


class Controller:

    def __init__(self, model: ModelAction) -> None:
        self.model = model

    def add_user(self, username: str, password: str) -> None:
        self.model.add_user(User(username, password))
