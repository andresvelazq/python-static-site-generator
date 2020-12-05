from pathlib import Path

class Site:
    # Constructor for class
    def __init__(self, source, dest):
        self.source = Path()
        self.dest = Path()

    # Find root directory
    def create_dir(self, path):
        directory = Path(self.dest / relative_to(self.source))
        directory.mkdir(parents=True, exist_ok=True)

    # Make the destination directory
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        # Recreate all paths
        for path in self.source.rglob("*"):
            if path.isdir():
                self.create_dir(path)
