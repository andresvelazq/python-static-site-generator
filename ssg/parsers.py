from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions.List[str] = []

    # Validates extensions
    def valid_extension(self, extension):
        if extension in self.extensions:
            return extension

    # Base class method
    def parse(path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        raise NotImplementedError

    def read(path):
        with open(path, 'r') as file:
            return file.read()

    def write(path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(self.path, self.dest / path.relative_to(self.source))
