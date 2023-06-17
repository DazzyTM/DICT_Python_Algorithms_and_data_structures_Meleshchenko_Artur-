from abstractlimitstructure_p5 import Stack, PriorQueue
import time
from class_generator import Generator

generator = Generator()
parrots = generator.generate_1000()

def test_stack_performance():
    stack = Stack()
    start_time = time.time()
    for parrot in parrots:
        stack.push(parrot)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert len(stack) == 1000
    assert elapsed_time < 1

def test_priorqueue_performance():
    prior_queue = PriorQueue()
    start_time = time.time()
    for parrot in parrots:
        prior_queue.enqueue(parrot)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert prior_queue.size() == 1000
    assert elapsed_time < 1
