from uuid import uuid4, UUID


class Category:
    def __init__(self, name: str, _id: UUID = uuid4(), description: str = None, is_active: bool = True):
        self.id = _id
        self.name = name
        self.description = description
        self.is_active = is_active

        if len(self.name) > 255:
            raise ValueError("name must have less than 256 characters")
