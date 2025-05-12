class DoublyLinkedList:
    class Node:
        def __init__(self, data, llink = None, rlink = None):
            self.data = data
            self.llink = llink
            self.rlink = rlink

    def __init__(self):
        self.head = None
        self.tail = None

    def clear(self):
        self.head = None
        self.tail = None

    def delete_head(self):
        data = self.head.data
        self.head = self.head.rlink
        if self.head == None:
            self.tail = None
        else:
            self.head.llink = None

        return data

    def delete_tail(self):
        data = self.tail.data
        self.tail = self.tail.llink
        if self.tail == None:
            self.head = None
        else:
            self.tail.rlink = None

        return data

    def display_head_to_tail(self):
        node = self.head
        while not node == None:
            print(node.data, end = " ")
            node = node.rlink

        print()

    def display_tail_to_head(self):
        node = self.tail
        while not node == None:
            print(node.data, end = " ")
            node = node.llink

        print()

    def insert_head(self, data):
        node = self.Node(data, None, self.head)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.llink = node
            self.head = node

    def insert_tail(self, data):
        node = self.Node(data, self.tail, None)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.rlink = node
            self.tail = node

    def is_empty(self):
        return self.head == None and self.tail == None