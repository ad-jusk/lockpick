from abc import ABC, abstractmethod

from src.model.entity.user import User


# ABSTRACT CLASS WITH METHOD DEFINITIONS THAT DIRECTLY MODIFY MODEL
class ModelAction(ABC):

    @abstractmethod
    def signup(self, name: str, surname: str, username: str, password: str) -> None: ...

    @abstractmethod
    def login(self, username: str, password: str) -> None: ...
