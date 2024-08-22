from src.model.entity.base import BaseEntity


class User(BaseEntity):

    def __init__(self, name: str, surname: str, username: str, password: str) -> None:
        super().__init__()
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
