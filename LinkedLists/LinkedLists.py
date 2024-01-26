class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
    
    def display_forward(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")