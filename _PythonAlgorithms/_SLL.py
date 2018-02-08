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

    def find_m_to_last_element(self, m):
        current = self.head
        for _ in range(m):
            if current.next:
                current = current.next
            else:
                return None

        m_behind = self.head

        while current.next:
            current = current.next
            m_behind = m_behind.next
        print("Data held within your desired mth(%d) element is: %d" % (m, m_behind.data))
        return m_behind

    def remove_head(self):
        temp = self.head
        if self.head.next is not None:
            temp = self.head.next
            del self.head
            self.head = temp
            print("There was a head")
            return True
        print("Error: No head to remove")
        return False


my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print "Element at 2nd index: %d" % my_list.get(2)

my_list.erase(1)
my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.append(10)
my_list.append(11)
my_list.display()
my_list.erase(5)

print("Element at 2nd index: %d" % my_list.get(2))

my_list.find_m_to_last_element(5)

my_list.display()
my_list.remove_head()
my_list.display()
