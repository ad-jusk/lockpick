from abc import ABC, abstractmethod

from src.model.entity.user import User


# ABSTRACT CLASS WITH METHOD DEFINITIONS THAT DIRECTLY MODIFY MODEL
class ModelAction(ABC):

    @abstractmethod
    def add_user(self, user: User) -> None: ...
