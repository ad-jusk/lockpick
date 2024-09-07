from src.database.database import Database
from src.model.entity.account import Account
from src.model.model_action import ModelAction
from src.model.model_data import ModelData
from src.model.entity.user import User

from typing import List
from typing_extensions import override


class Model(ModelAction, ModelData):

    def __init__(self, database: Database) -> None:
        self.database = database

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
