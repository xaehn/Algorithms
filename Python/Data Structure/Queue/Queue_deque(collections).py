from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def clear(self):
        self.queue.clear()

    def dequeue(self):
        return self.queue.popleft()

    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __len__(self):
        return len(self.queue)