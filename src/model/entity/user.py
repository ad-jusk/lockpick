from src.model.entity.base import BaseEntity


class User(BaseEntity):

    def __init__(self, name: str, surname: str, username: str, password: str) -> None:
        super().__init__()
        self.__name = name
        self.__surname = surname
        self.__username = username
        self.__password = password

    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password
