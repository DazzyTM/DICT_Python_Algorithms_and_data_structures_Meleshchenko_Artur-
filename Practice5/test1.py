import pytest
from class_parrot import Parrot
from abstractlimitstructure_p5 import Stack, PriorQueue


class TestStack:
    def test_push_pop(self):
        stack = Stack()
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        parrot2 = Parrot("Parrot2", "Breed2", "Color2", 2, 5)
        parrot3 = Parrot("Parrot3", "Breed3", "Color3", 3, 3)
        stack.push(parrot1)
        stack.push(parrot2)
        stack.push(parrot3)
        assert stack.pop() == parrot3
        assert stack.pop() == parrot2
        assert stack.pop() == parrot1

    def test_pop_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    def test_top(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.top()
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        stack.push(parrot1)
        assert stack.top() == parrot1

    def test_len(self):
        stack = Stack()
        assert len(stack) == 0
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        stack.push(parrot1)
        assert len(stack) == 1

    def test_repr(self):
        stack = Stack()
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        parrot2 = Parrot("Parrot2", "Breed2", "Color2", 2, 5)
        stack.push(parrot1)
        stack.push(parrot2)
        expected_repr = (
            "[Parrot(Parrot2, Breed2, Color2, 2, 5), Parrot(Parrot1, Breed1, Color1, 1, 4)]"
        )
        assert repr(stack) == expected_repr


class TestPriorQueue:
    def test_enqueue_dequeue(self):
        queue = PriorQueue()
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        parrot2 = Parrot("Parrot2", "Breed2", "Color2", 2, 5)
        parrot3 = Parrot("Parrot3", "Breed3", "Color3", 3, 3)
        queue.enqueue(parrot1)
        queue.enqueue(parrot2)
        queue.enqueue(parrot3)
        assert queue.dequeue().size == 3

    def test_dequeue_empty_queue(self):
        queue = PriorQueue()
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_is_empty(self):
        queue = PriorQueue()
        assert queue.is_empty()
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        queue.enqueue(parrot1)
        assert not queue.is_empty()

    def test_size(self):
        queue = PriorQueue()
        assert queue.size() == 0
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        queue.enqueue(parrot1)
        assert queue.size() == 1

    def test_peek(self):
        queue = PriorQueue()
        with pytest.raises(IndexError):
            queue.peek()
        parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        queue.enqueue(parrot1)
