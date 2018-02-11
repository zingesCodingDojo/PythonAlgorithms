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


"""
Carlos Version!

Wooo
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = Node()

    def append(self, index=None, data=None):
        if data is None:
            print("ERROR: 'Linked List will NOT accept data of None.'")
            return False

        new_node = Node(data)
        current_index = 0
        current_node = self.head

        if index is 0:
            if current_node.next is None:
                current_node.next = new_node
                return True

            else:
                temp = current_node.next
                current_node.next = new_node
                new_node.next = temp
                return True

        if index > self.length():
            print("ERROR: 'Get index is out of range! Cannot append.'")
            return False

        while current_node.next is not None:
            if current_index == index:
                temp = current_node.next
                current_node.next = new_node
                new_node.next = temp
                return True

            current_node = current_node.next
            current_index += 1
        current_node.next = new_node
        return True

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next is not None:
            total += 1
            current_node = current_node.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        if current_node.next is None:
            elements.append(current_node.data)
            print(elements)
            return
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get index is out of range!")
            return None
        current_index = 0
        current_node = 0
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index=None, try_data=None):
        current_index = 0
        current_node = self.head
        if index is None and try_data is None:
            print("ERROR: 'Will not delete if Index is None and Data is None. Check arguments'")
            return False
        else:
            if index >= self.length():
                print("ERROR: 'Get index is out of range!")
                return None

        while current_index != self.length():
            last_node = current_node
            current_node = current_node.next
            if last_node.data is not None:
                if current_node.data == try_data:
                    # print("Found the value! %s" % current_node.data)
                    last_node.next = current_node.next
                    return True
            if current_index == index:
                last_node.next = current_node.next
                return True
            current_index += 1

        print("Desired data to delete was not found.")
        del try_data
        return False

    def find_m(self, m):
        current_node = self.head
        for _ in range(m):
            if current_node.next:
                current_node = current_node.next
            else:
                print("ERROR: 'Your desired input is not found.'")
                return None
        m_behind = self.head

        while current_node.next:
            current_node = current_node.next
            m_behind = m_behind.next
        return m_behind

    def remove_head(self):
        if self.head.next is not None:
            temp = self.head.next
            del self.head
            self.head = temp
            print("Head found")
            return True
        print("ERROR: No head to remove.")
        return False


my_list = SLL()
my_list.append(index=0, data=20)
my_list.append(data=1)
my_list.append(index=0, data=5)
my_list.append(data=2)
my_list.append(data=3)
my_list.append(data=4)
my_list.append(data=5)
my_list.append(index=int(my_list.length()), data=42)
my_list.append(data=6)

my_list.display()
my_list.erase(index=4, try_data=None)
my_list.display()
