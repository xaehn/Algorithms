class Stack:
    def __init__(self):
        self.top = []

    def clear(self):
        self.top = []

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

    def __len__(self):
        return len(self.top)