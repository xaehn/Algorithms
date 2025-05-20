import heapq

class MinHeapPriorityQueue:
    def __init__(self):
        self.queue = []

    def clear(self):
        self.queue.clear()

    def dequeue(self):
        return heapq.heappop(self.queue)[1][1]

    def enqueue(self, priority, item):
        heapq.heappush(self.queue, (priority, item))

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0][1]

    def peek_priority(self):
        return self.queue[0][0]

    def size(self):
        return len(self.queue)

    def __len__(self):
        return len(self.queue)

# if priority == item
class MinHeapPriorityQueue:
    def __init__(self):
        self.queue = []

    def clear(self):
        self.queue.clear()

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def enqueue(self, priority):
        heapq.heappush(self.queue, priority)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __len__(self):
        return len(self.queue)