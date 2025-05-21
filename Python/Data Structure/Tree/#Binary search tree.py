from collections import deque

class BinarySearchTree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.count = 0

    def delete_node(self, key):
        pass

    def find_node(self, key):
        node = self.root
        while not node == None:
            if node.key == key:
                return True
            elif node.key < key:
                node = node.left
            else:
                node = node.right

        return False

    def insert_node(self, key):
        if self.root == None:
            self.root = self.Node(key)
            self.count += 1
            return

        node = self.root
        while True:
            if node.key < key:
                if node.right == None:
                    node.right = self.Node(key)
                    node.count += 1
                    return
                else:
                    node = node.right
            else:
                if node.left == None:
                    node.left = self.Node(key)
                    self.count += 1
                    return
                else:
                    node = node.left