from .base import BaseEntity

# REPRESENTS ACCOUNT WHOSE DATA USER WANTS TO SAVE
class Account(BaseEntity):

    def __init__(self, title: str, email: str, password: str, tip: str) -> None:
        super().__init__()
        self.title = title
        self.email = email
        self.password = password
        self.tip = tip

    def get_title(self) -> str:
        return self.title

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password

    def get_tip(self) -> str:
        return self.tip