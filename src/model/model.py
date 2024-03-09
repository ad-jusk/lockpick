from ..logger import LOGGER
from .model_action import ModelAction
from .model_data import ModelData
from .entity.user import User

class Model(ModelAction, ModelData):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)
        return cls.instance
    
    def add_user(self, user: User):
        LOGGER.info(f"User {user.get_username()} added")
    
    def get_users(self):
        LOGGER.info("Got users")