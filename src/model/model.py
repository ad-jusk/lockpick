from log.logger import LOGGER
from src.model.model_action import ModelAction
from src.model.model_data import ModelData
from src.model.entity.user import User

from typing import Type, TypeVar

T = TypeVar("T", bound="Model")


class Model(ModelAction, ModelData):

    def __new__(cls: Type[T]) -> T:
        if not hasattr(cls, "instance"):
            cls.instance = super(Model, cls).__new__(cls)
        return cls.instance

    def add_user(self, user: User) -> None:
        LOGGER.info(f"User {user.get_username()} added")

    def get_users(self) -> None:
        LOGGER.info("Got users")
