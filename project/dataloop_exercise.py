from typing import Optional


class Data:
    class Metadata:
        class System:
            def __init__(self, size: Optional[(float)] = None, height: Optional[float] = None,**kwargs):
                 # Validation
                if size is not None and not isinstance(size, (int, float)):
                    raise ValueError("size should be either None or of type number.")
                if height is not None and not isinstance(height, (int, float)):
                    raise ValueError("height should be either None or of type int.")
                # size and heihgt to float
                if size is not None:
                    self.size = float(size)
                if height is not None:
                    self._height = float(height)

            @property
            def height(self) -> int:
                if self._height is None:
                    self._height = 100
                return self._height

        class User:
            def __init__(self, batch: Optional[int] = None,**kwargs):
                # Validation
                if batch is not None and not isinstance(batch, int):
                    raise ValueError("batch should be either None or of type int.")
                self.batch = batch

        def __init__(self, system: Optional['Data.Metadata.System'] = None, user: Optional['Data.Metadata.User'] = None,**kwargs):
            if system:
                self.system = self.System(**system)
            else:
                self.system = self.System()

            if user:
                self.user = self.User(**user)
            else:
                self.user = self.User()

    def __init__(self, id: Optional[str] = None, name: Optional[str] = None, metadata: Optional['Data.Metadata'] = None,**kwargs):

        if id is not None and not isinstance(id, (int, str)):
            raise ValueError("id should be either None or of type str or int.")
        if name is not None and not isinstance(name, str):
            raise ValueError("name should be either None or of type str.")
        if id is not None:
            self.id = str(id)
        self.name = name
        self.metadata: 'Data.Metadata'  # Type hint for metadata

        if metadata:
            self.metadata = self.Metadata(**metadata)
        else:
            self.metadata = self.Metadata()

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "metadata": {
                "system": {
                    "size": self.metadata.system.size,
                    "height": self.metadata.system.height
                },
                "user": {
                    "batch": self.metadata.user.batch
                }
            }
        }

    @property
    def size(self):
        return self.metadata.system.size

    @property
    def height(self):
        return self.metadata.system.height

    @height.setter
    def height(self, value):
        self.metadata.system.height = value