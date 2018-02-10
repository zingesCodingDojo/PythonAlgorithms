

class SinglyNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = SinglyNode()

    def append(self, data):
        new_node = SinglyNode(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

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
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)

        print(elements)

    def get(self, index):
        if index >= self.length():
            return None, "Error: Get index is out of range."

        current_index = 0
        current_node = self.head

        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            return None, "Error: Get index is out of range. Cannot erase what I cannot see!"

        current_index = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


my_SSL = SLL()
my_SSL.append(1)
my_SSL.append(2)
my_SSL.append(3)
my_SSL.append(4)
my_SSL.append(5)
my_SSL.append(6)

print(my_SSL.display())

my_SSL.erase(4)
print(my_SSL.display())


