from log.logger import LOGGER
from src.model.entity.account import Account
from src.model.model_action import ModelAction
from src.model.model_data import ModelData
from src.model.entity.user import User

from typing import List, Type, TypeVar
from typing_extensions import override

T = TypeVar("T", bound="Model")


class Model(ModelAction, ModelData):

    def __new__(cls: Type[T]) -> T:
        if not hasattr(cls, "instance"):
            cls.instance = super(Model, cls).__new__(cls)
        return cls.instance

    @override
    def signup(self, name: str, surname: str, username: str, password: str) -> None:
        pass

    @override
    def login(self, username: str, password: str) -> None:
        pass

    @override
    def get_user(self) -> User:
        pass

    @override
    def get_accounts(self) -> List[Account]:
        pass
