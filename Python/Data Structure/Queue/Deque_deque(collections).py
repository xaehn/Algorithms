from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def append_l(self, item):
        self.deque.appendleft(item)

    def append_r(self, item):
        self.deque.append(item)

    def clear(self):
        self.deque.clear()

    def is_empty(self):
        return len(self.deque) == 0
    
    def peek_l(self):
        return self.deque[0]

    def peek_r(self):
        return self.deque[-1]
    
    def pop_l(self):
        return self.deque.popleft()

    def pop_r(self):
        return self.deque.pop()
    
    def rotate_l(self, n = 1):
        self.deque.rotate(-n)

    def rotate_r(self, n = 1):
        self.deque.rotate(n)

    def size(self):
        return len(self.deque)