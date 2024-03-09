from ..model.entity.user import User
from ..model.model_action import ModelAction

class Controller:

    def __init__(self, model: ModelAction):
        self.model = model
    
    def add_user(self, username: str, password: str):
        self.model.add_user(User(username, password))
        