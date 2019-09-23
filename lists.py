class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.root = None

    def print(self):
        if self.root is None:
            print("/empty")
        else:
            n = self.root
            while n is not None:
                print(n.cargo)
                n = n.next

    def get_tail(self):
        last_node = self.root
        if self.root is None:
            return self.root
        while last_node.next is not None:
            last_node = last_node.next
        return last_node
        
    def push_front(self, value):
        new_node = Node(value, self.root)
        new_node.next = self.root
        self.root = new_node

        
    def push_back(self, value):
        new_node = Node(value)
        tail = self.get_tail()
        if tail is None:
            self.root = new_node
            return
        tail.next = new_node

    def pop_front(self):
        if self.root is None:
            print("/empty")
        else:
            self.root = self.root.next
    
    def pop_back(self):
        if self.root is None:
            print("/empty")
        else:
            ante_last = self.root
            last = ante_last.next
            if last is None:
                self.root = None
            elif last.next is None:
                ante_last.next = None
            else:
                while last.next is not None:
                    ante_last = last
                    last = last.next
                ante_last.next = None
