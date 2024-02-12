from _typeshed import Incomplete

from antlr4.Token import Token as Token

class InputStream:
    name: str
    strdata: Incomplete
    data: Incomplete
    def __init__(self, data: str) -> None: ...
    @property
    def index(self): ...
    @property
    def size(self): ...
    def reset(self) -> None: ...
    def consume(self) -> None: ...
    def LA(self, offset: int): ...
    def LT(self, offset: int): ...
    def mark(self): ...
    def release(self, marker: int): ...
    def seek(self, _index: int): ...
    def getText(self, start: int, stop: int): ...
