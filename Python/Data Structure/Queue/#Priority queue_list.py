import heapq

class PriorityQueue:
    def __init__(self, minimum = True):
        self.minimum = minimum
        self.queue = []

    def clear(self):
        self.queue.clear()

    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    
    def enqueue(self, priority, item):
        if self.minimum:
            heapq.heappush(self.queue, (priority, item))
        else:
            heapq.heappush(self.queue, (-priority, item))

    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        return self.queue[0][1]
    
    def peek_priority(self):
        return self.queue[0][0] if self.minimum else -self.queue[0][0]
    
    def size(self):
        return len(self.queue)