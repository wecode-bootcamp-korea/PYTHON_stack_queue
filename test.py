import pytest
from stack import Stack
from q import Queue

class TestClass:

    def test_stack_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1

    def test_getPeak(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(4)
        assert s.getPeak() == 4
        s.pop()
        assert s.getPeak() == 2
        s.pop()
        assert s.getPeak() == 1

    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(2)
        assert q.dequeue() == 2

    def test_getFirst(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(4)
        assert q.getFirst() == 1
        assert q.dequeue() == 1
        assert q.getFirst() == 2
        assert q.dequeue() == 2
        assert q.getFirst() == 4
        assert q.dequeue() == 4