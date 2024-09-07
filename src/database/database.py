import sqlite3

from src.database.query import UserQuery
from src.model.entity.user import User


class Database:

    def __init__(self, database_path: str) -> None:
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

        self.cursor.execute(UserQuery.CREATE_TABLE.value)
        self.connection.commit()

    def add_user(self, user: User) -> None:
        pass
