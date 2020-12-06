from collections.abc import Mapping
import load
import re
from yaml import FullLoader

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        (_, fm, content) = split(__regex, string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        data = metadata
        self.data = {
            "content": content
        }

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if self.data else None

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return

    def __len__(self):
        return self.data.length

    def __repr__(self):
        data = {}
        return str(data)
