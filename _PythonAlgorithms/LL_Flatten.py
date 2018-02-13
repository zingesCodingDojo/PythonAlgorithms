
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

    def add_child(self, child):
        current_child = Node()

    def append(self, index=None, data=None, child=None):
        """
        Easier manner to digest this code would be to split the method into two different methods.
        One to insert at END (or start) and one to insert at INDEX.
        :param index: Desired index position of new Node.
        :param data:  Data being appended to DoublyLinkedList
        :return: True if append is successful. False if failure accurs.
        """
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

                # print("Previous data is: %s %s" % (current_node.prev.data, new_node.prev.data))
                return True
            current_node = current_node.next
            current_index += 1

        temp = current_node.next
        current_node.next = new_node
        new_node.next = temp
        new_node.prev = current_node
        self.tail = new_node
        # print("I have added to the end of the list!: %s" % new_node.data)
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
        first_child = []
        current_node = self.head
        if current_node.next is None:
            elements.append(current_node.data)
            return
        while current_node is not None:
            if current_node.child is not None:
                first_child.append(current_node.child.data)
            elements.append(current_node.data)
            current_node = current_node.next
        print("Level 1 elemets: %s" % elements,
              "Level 2 elements: %s" % first_child)

    def backward_display(self):
        elements = []
        current_node = self.tail
        if current_node.prev is None:
            elements.append(current_node.data)
            return False
        while current_node.prev is not None:
            # print(current_node.data)
            elements.append(current_node.data)
            current_node = current_node.prev
        elements.append(current_node.data)
        print(elements)

    def remove_head(self):
        if self.head.next is not None:
            temp = self.head.next
            del self.head
            self.head = temp
            self.head.prev = None
            return True
        print("ERROR: 'No head to remove.'")
        return False


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
test_me.remove_head()
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


def flatten_list(head, tail):
    current_node = head
    while current_node.next is not None:
        if current_node.child is not None:
            append_child(current_node.child, tail)
        current_node = current_node.next


def append_child(child, tail):
    current_node = child
    tail.next = child
    child.prev = tail

    while current_node == child:
        current_node = current_node.next
    tail = current_node


def unflatten_list(start, tail):
    #current_node = None

    explore_and_seperate(start)

    current_node = start
    while current_node.next is not None:
        current_node = current_node.next
    tail = current_node


def explore_and_seperate(childListStart):
    current_node = childListStart
    while current_node:
        if current_node.child is not None:
            current_node.child.prev.next = None
            current_node.child.prev = None
            explore_and_seperate(current_node.child)
        current_node = current_node.next
