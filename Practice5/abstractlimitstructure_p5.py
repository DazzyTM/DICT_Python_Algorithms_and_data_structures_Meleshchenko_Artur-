from method import AbstractStack, PriorityQueue
from class_parrot import Parrot

class Node:
    def __init__(self, value: Parrot, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack(AbstractStack):
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, value: Parrot) -> None:
        new_node = Node(value)
        if self.__top is None:
            self.__top = new_node
        else:
            new_node.next_node = self.__top
            self.__top = new_node
        self.__size += 1

    def pop(self) -> Parrot:
        if self.__top is None:
            raise IndexError("Stack is empty")
        node_to_remove = self.__top
        self.__top = self.__top.next_node
        self.__size -= 1
        return node_to_remove.value

    def top(self) -> Parrot:
        if self.__top is None:
            raise IndexError("Stack is empty")
        return self.__top.value

    def __repr__(self) -> str:
        items = []
        current_node = self.__top
        while current_node is not None:
            items.append(str(current_node.value))
            current_node = current_node.next_node
        return '[' + ', '.join(items) + ']'

    def __len__(self) -> int:
        return self.__size

class PriorQueue(PriorityQueue):
    def __init__(self):
        self.head = None

    def enqueue(self, value: Parrot):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            prev = None
            while current is not None and current.value.size > value.size:
                prev = current
                current = current.next_node
            if prev is None:
                new_node.next_node = self.head
                self.head = new_node
            else:
                prev.next_node = new_node
                new_node.next_node = current

    def dequeue(self) -> Parrot:
        if self.is_empty():
            raise IndexError("Queue is empty")
        dequeued_node = self.head
        self.head = self.head.next_node
        return dequeued_node.value

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def peek(self) -> Parrot:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.value

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        items = []
        current_node = self.head
        while current_node is not None:
            items.append(str(current_node.value))
            current_node = current_node.next_node
        return '[' + ', '.join(items) + ']'

    def top(self) -> Parrot:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.value
