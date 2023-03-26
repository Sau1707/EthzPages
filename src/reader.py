import itertools
from typing import Generator

class Reader:
    def __init__(self, filename, limiter=None) -> None:
        self.filename = filename
        self.limiter = limiter

        with open(self.filename, "r") as f:
            self.len = sum(1 for line in f)
    
    def __iter__(self) -> Generator[str, None, None]:
        if self.limiter:
            with open(self.filename, "r") as file:
                for name in itertools.islice(file, self.limiter):
                    yield name.strip()
        else:
            for name in open(self.filename, "r"):
                yield name.strip()

    def __len__(self) -> int:
        if self.limiter:
            return self.limiter
        return self.len