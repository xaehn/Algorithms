from collections import deque

class Stack:
    def __init__(self):
        self.top = deque()

    def clear(self):
        self.top.clear()

    def is_empty(self):
        return len(self.top) == 0

    def peek(self):
        return self.top[-1]

    def pop(self):
        return self.top.pop()

    def push(self, item):
        self.top.append(item)

    def size(self):
        return len(self.top)