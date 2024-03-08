from base import BaseEntity

class User(BaseEntity):

    def __init__(self, username: str, password: str) -> None:
        super.__init__()
        self.username = username
        self.password = password
    
    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password