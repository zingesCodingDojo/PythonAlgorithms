
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, index=None, data=None):
        if data is None:
            print("ERROR: 'Linked List will NOT accept data of None nor negative Index!'")
            return False

        if index is None:
            pass

        new_node = Node(data)
        current_index = 1
        current_node = self.head

        if self.head is None:
            self.head = self.tail = new_node
            print("added my first node")
            return True

        if index == 0:
            current_node.prev = new_node
            new_node.next = current_node
            self.head = new_node
            return True

        while current_node.next is not None:
            if current_index == index and index != self.length():
                backwards = current_node.prev
                current_node.prev = new_node
                new_node.next = current_node
                backwards.next = new_node
                new_node.prev = backwards

                print("Previous data is: %s %s" % (current_node.prev.data, new_node.prev.data))
                return True
            current_node = current_node.next
            current_index += 1

        temp = current_node.next
        current_node.next = new_node
        new_node.next = temp
        new_node.prev = current_node
        self.tail = new_node
        print("I have added to the end of the list!: %s" % new_node.data)
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
            return
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def backward_display(self):
        elements = []
        current_node = self.tail
        if current_node.prev is None:
            elements.append(current_node.data)
            return False
        while current_node.prev is not None:
            print(current_node.data)
            elements.append(current_node.data)
            current_node = current_node.prev
        elements.append(current_node.data)
        print(elements)


test_me = DoublyLinkedList()
test_me.append(data=1)
test_me.append(data=2)
test_me.append(data=3)
test_me.append(data=4)
test_me.append(data=5)
test_me.append(index=2, data=42)
test_me.append(index=0, data=206)
test_me.append(index=5, data=115)
test_me.display()
test_me.backward_display()

    # def length(self):
    #     current_node = self.head
    #     total = 0
    #     while current_node.next is not None:
    #         total += 1
    #         current_node = current_node.next
    #     return total
    #
    # def display(self):
    #     elements = []
    #     current_node = self.head
    #     if current_node.next is None:
    #         elements.append(current_node.data)
    #         print(elements)
    #         return
    #     while current_node.next is not None:
    #         current_node = current_node.next
    #         elements.append(current_node.data)
    #     print(elements)


class FlattenLinkedList:
    def __init__(self):
        self.head = Node()

    def flatten_list(self):
        current_node = self.head

        while current_node.next is not None:
            if current_node.child:
                self.append(current_node.child, current_node.tail)

            current_node = current_node.next

    def append(self, child, tail):
        current_node = self.head

        current_node.tail = child
        child.prev = tail

        while current_node.child and current_node.next:
            current_node = current_node.next

        current_node.next = current_node


# my_list = DoublyLinkedList()
# my_list.append(data=5)
# my_list.display()
