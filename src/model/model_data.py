from abc import ABC, abstractmethod
from typing import List

from src.model.entity.account import Account
from src.model.entity.user import User


# ABSTRACT CLASS WITH METHOD DEFINITIONS THAT DO NOT MODIFY MODEL
class ModelData(ABC):

    @abstractmethod
    def get_user(self) -> User: ...

    @abstractmethod
    def get_accounts(self) -> List[Account]: ...
