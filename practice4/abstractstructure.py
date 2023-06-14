from abc import ABC, abstractmethod
from collections.abc import Iterable
from class_parrot import Parrot


class AbstractStructureBasic(ABC):

    @abstractmethod
    def __init__(self, *args: Iterable[Parrot]):
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, key) -> Parrot:
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def append(self, value: Parrot) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, value: Parrot) -> None:
        pass

    @abstractmethod
    def index(self, value: Parrot, start: int = 0, stop: int = -1) -> int:
        pass

    @abstractmethod
    def remove(self, value: Parrot) -> None:
        pass
