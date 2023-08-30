from typing import Optional


class Data:
    class Metadata:
        class System:
            def __init__(self, size: Optional[float] = None, height: Optional[int] = None):
                self.size = size
                self._height = height

            @property
            def height(self) -> int:
                if self._height is None:
                    self._height = 100
                return self._height

        class User:
            def __init__(self, batch: Optional[int] = None):
                self.batch = batch

        def __init__(self, system: Optional['Data.Metadata.System'] = None, user: Optional['Data.Metadata.User'] = None):
            if system:
                self.system = self.System(**system)
            else:
                self.system = self.System()

            if user:
                self.user = self.User(**user)
            else:
                self.user = self.User()

    def __init__(self, id: Optional[str] = None, name: Optional[str] = None, metadata: Optional['Data.Metadata'] = None):
        self.id = id
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


# Usage from dictionary
data = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 10
        }
    }
}


# load from dict
my_inst_1 = Data.from_dict(data)

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.size)  # should print 10.7

# default values
# should set a default value of 100 in metadata.system.height
print(my_inst_1.height)
print(my_inst_1.to_dict()['metadata']['system']
      ['height'])  # should print the default value
