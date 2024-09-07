from .base import BaseEntity


# REPRESENTS ACCOUNT WHOSE DATA USER WANTS TO SAVE
class Account(BaseEntity):

    def __init__(self, title: str, email: str, password: str, tip: str) -> None:
        super().__init__()
        self.__title = title
        self.__email = email
        self.__password = password
        self.__tip = tip

    def get_title(self) -> str:
        return self.__title

    def get_email(self) -> str:
        return self.__email

    def get_password(self) -> str:
        return self.__password

    def get_tip(self) -> str:
        return self.__tip
