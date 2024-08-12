from abc import ABC, abstractmethod


# ABSTRACT CLASS WITH METHOD DEFINITIONS THAT DO NOT MODIFY MODEL
class ModelData(ABC):

    @abstractmethod
    def get_users(self) -> None: ...
