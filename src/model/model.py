from src.logger import LOGGER
from src.model.model_action import ModelAction
from src.model.model_data import ModelData
from src.model.entity.user import User


class Model(ModelAction, ModelData):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Model, cls).__new__(cls)
        return cls.instance

    def add_user(self, user: User):
        LOGGER.info(f"User {user.get_username()} added")

    def get_users(self):
        LOGGER.info("Got users")
