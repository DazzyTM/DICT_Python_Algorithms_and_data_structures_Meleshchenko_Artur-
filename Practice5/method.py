from abc import ABC, abstractmethod
from class_parrot import Parrot

class AbstractStack(ABC):

    @abstractmethod
    def push(self, value: Parrot) -> None:
        pass

    @abstractmethod
    def pop(self) -> Parrot:
        pass

    @abstractmethod
    def top(self) -> Parrot:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass


class PriorityQueue(ABC):

    @abstractmethod
    def enqueue(self, value: Parrot) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Parrot:
        pass

    @abstractmethod
    def top(self) -> Parrot:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass
