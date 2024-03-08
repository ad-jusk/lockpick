from datetime import datetime
from uuid import uuid4, UUID
from typing import Final

class BaseEntity:

    def __init__(self) -> None:
        self.id: Final[UUID] = uuid4()
        self.created: Final[str] = datetime.now().strftime("%d.%m.%Y %H:%M")

    def get_id(self) -> UUID:
        return self.id
    
    def get_created(self) -> str:
        return self.created
