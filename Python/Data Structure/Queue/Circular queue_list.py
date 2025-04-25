class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = self.max_size * [None]
        self.front = 0
        self.rear = 0
    
    def clear(self):
        self.front = 0
        self.rear = 0

    def dequeue(self):
        self.front = (self.front + 1) % self.max_size
        return self.queue[self.front]
    
    def enqueue(self, item):
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front
    
    def peek(self):
        return self.queue[(self.front + 1) % self.max_size]
    
    def size(self):
        return (self.rear - self.front + self.max_size) % self.max_size