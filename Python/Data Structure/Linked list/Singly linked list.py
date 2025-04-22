class SinglyLinkedList:
    class Node:
        def __init__(self, data, link = None):
            self.data = data
            self.link = link

    def __init__(self):
        self.head = None

    def clear(self):
        self.head = None

    def delete_node(self, position):
        node = self.head
        if position == 0:
            self.head = self.head.link
        else:
            for _ in range(position - 1):
                node = node.link

            node.link = node.link.link

    def find_data(self, data):
        node = self.head
        while not node == None:
            if node.data == data:
                return node

            node = node.link

        return node

    def get_data(self, position):
        node = self.head
        for _ in range(position):
            node = node.link

        return node.data

    def get_node(self, position):
        node = self.head
        for _ in range(position):
            node = node.link

        return node
    
    def insert_node(self, position, data):
        node = self.head
        for _ in range(position - 1):
            node = node.link

        if node == None:
            self.head = Node(data, self.head)
        else:
            new_node = Node(data, node.link)
            node.link = new_node

    def is_empty(self):
        return self.head == None
    
    def replace_data(self, position, data):
        node = self.head
        for _ in range(position):
            node = node.link

        node.data = data

    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1

        return count