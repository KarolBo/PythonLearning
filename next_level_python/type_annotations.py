from typing import Protocol

my_int: int = 10

my_dict: dict[str, int] = {
    'chuj': 5,
    'kurwa': 10,
    'dupa': 4,
    'cipa': 7
}

optional1: int | None = 5
optional2: int | None = None

my_tuple: tuple[int | str, ...] = (1, 2, 3, 'a', 'b', 'c')


class EmailServer(Protocol):
    @property
    def _host(self) -> str:
        ...

    def connect(self, host: str, port: int) -> None:
        ...

    def login(self, login: str, password: str) -> None:
        ...

    
class EmailClient:
    def __init__(self, 
                 smtp_server: EmailServer,
                 login: str,
                 password: str):
        self._server = smtp_server
        self._login = login
        self._password = password