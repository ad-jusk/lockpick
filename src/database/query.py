from enum import Enum


class UserQuery(Enum):
    CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS users (
            id Varchar(255) PRIMARY KEY,
            created Varchar(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    """
    INSERT_INTO = """
        INSERT INTO users
        (id, created, name, surname, username, password)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    SELECT_ALL = """SELECT * FROM users"""
