class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev
    
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def last_element(self):
        current = self.head
        while current.next:
            current = current.next
        return current
    
    def print_forward(self):
        if self.head is None:
            print('Empty Linked List')
            return
        
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def print_backward(self):
        if self.head is None:
            print('Empty Linked List')
            return
        
        last_node = self.last_element()
        current = last_node
        while current:
            print(current.value)
            current = current.prev

    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return
        
        current = self.head
        while current.next:
            current = current.next
        node = Node(data, None, current)
        current.next = node
    
    def insert_at(self, position, data):
        if position < 0 or position > self.length():
            raise IndexError('Invalid Index')
        
        if position == 0:
            self.insert_at_start(data)
            return
        
        pos = 0
        current = self.head
        while current:
            if pos == position - 1:
                node = Node(data, current.next, current)
                if node.next:
                    current.next.prev = node
                current.next = node
                break
            current = current.next
            pos += 1

    def insert_after(self, data_after, data_to_insert):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.value == data_after:
                node = Node(data_to_insert, current.next, current)
                if node.next:
                    current.next.prev = node
                current.next = node
                return
            current = current.next

        raise ValueError('Invalid After Value')

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, position):
        if position < 0 or position >= self.length():
            raise IndexError('Invalid Index')

        if position == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        pos = 0
        current = self.head
        while current:
            if pos == position:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                break
            current = current.next
            pos += 1

    def remove_value(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head
        while current:
            if current.value == value:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                break
            current = current.next

        raise ValueError('Invalid Value')
