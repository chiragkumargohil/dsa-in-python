class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def show_linked_list(self):
        if self.head is None:
            print(None)
            return
        
        current = self.head
        while current:
            print(current.value, end=' <--> ')
            current = current.next
        print()

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element(self, position):
        pos = 0
        current = self.head
        while current:
            if pos == position:
                return current.value
            pos += 1
            current = current.next
        raise IndexError('Invalid Index')

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def insert_at(self, position, data):
        if position < 0 or position > self.length():
            raise IndexError('Invalid Index')
        
        if position == 0:
            self.insert_at_start(data)
            return

        pos = 0
        current = self.head
        while current:
            if pos == position-1:
                node = Node(data, current.next)
                current.next = node
            pos += 1
            current = current.next
    
    def insert_after(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        current = self.head
        while current:
            if current.value == data_after:
                node = Node(data_to_insert, current.next)
                current.next = node
                return
            current = current.next
        
        raise ValueError('Invalid After Value')

    def insert_list(self, data_list: list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def remove_at(self, position):
        if position < 0 or position >= self.length():
            raise IndexError('Invalid Index')
        
        if position == 0:
            self.head = self.head.next
            return
        
        pos = 0
        current = self.head
        while current:
            if pos == position - 1:
                current.next = current.next.next
                break
            current = current.next
            pos += 1

    def remove_value(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError('Invalid Value')
