from _Nodes import Node as node


"""
This is the Singly Linked List Class.
We will be able to add, remove, edit, and check for circular movements.
"""

# Gotta track the head element so not to lose the list as traversing the list! Losing the head will mean losing it in
# memory.


class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get index is out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Get index is out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print "Element at 2nd index: %d" % my_list.get(2)


my_list.erase(1)
my_list.display()


"""
This is the Doubly Linked List Class.
We will be able to add, remove, edit, traverse both forwards and backwards, and check for circular movements.
"""

"""
This is the Circular Linked List Class.
We will be able to add, remove, edit, traverse.
"""