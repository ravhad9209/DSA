class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert at position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            self.insert_begin(data)
            return
        
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_begin(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if not self.head:
            print("List is empty")
            return
        
        if not self.head.next:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete by value
    def delete_value(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print("Value not found")
            return
        
        prev.next = temp.next

    # Search element
    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

