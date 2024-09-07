from datetime import datetime
from uuid import uuid4, UUID
from typing import Final


class BaseEntity:

    def __init__(self) -> None:
        self.__id: Final[UUID] = uuid4()
        self.__created: Final[str] = datetime.now().strftime("%d.%m.%Y %H:%M")

    def get_id(self) -> UUID:
        return self.__id

    def get_created(self) -> str:
        return self.__created
