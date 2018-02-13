class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = Node()
        self.size = 0

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

            elif current_node.next is not None:
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
            return None
        elif index == 0:
            self.remove_head()
            return None
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

        if m >= self.length():
            print("ERROR: 'Your desired input is not within allowed range.")
            return None

        for _ in xrange(m):
            if current_node.next:
                current_node = current_node.next

        m_behind = self.head

        while current_node.next:
            current_node = current_node.next
            m_behind = m_behind.next
        print(m_behind.data)
        return m_behind

    def remove_head(self):
        if self.head.next is not None:
            temp = self.head.next
            del self.head
            self.head = temp
            return True
        print("ERROR: No head to remove.")
        return False


if __name__ == "__main__":
    pass
    # my_list = SLL()
    #
    # my_list.erase(index=0)
    # my_list.append(index=0, data=20)
    # my_list.append(data=1)
    # my_list.append(index=0, data=5)
    # my_list.append(data=2)
    # my_list.append(data=3)
    # my_list.append(data=4)
    # my_list.append(data=5)
    # my_list.append(index=int(my_list.length()), data=42)
    # my_list.append(data=6)
    #
    # my_list.display()
    # my_list.erase(index=0, try_data=None)
    # my_list.erase(index=0, try_data=None)
    # my_list.display()
    # my_list.erase(try_data=42)
    # my_list.append(index=0, data=17)
    # my_list.append(index=0, data=8)
    # my_list.append(data=9)
    # my_list.display()
    # my_list.find_m(7)
    # for _ in xrange(100):
    #     my_list.append(data=_)
    # my_list.display()

    # class Person:
    #     TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
    #
    #     def __init__(self, name, surname):
    #         self.name = name
    #         self.surname = surname
    #
    #     def fullname(self): # instance method
    #         # instance object accessible through self
    #         return "%s %s" % (self.name, self.surname)
    #
    #     @classmethod
    #     def allowed_titles_starting_with(cls, startswith): # class method
    #         # class or instance object accessible through cls
    #         return [t for t in cls.TITLES if t.startswith(startswith)]
    #
    #     @staticmethod
    #     def allowed_titles_ending_with(endswith): # static method
    #         # no parameter for class or instance object
    #         # we have to use Person directly
    #         return [t for t in Person.TITLES if t.endswith(endswith)]
    #
    #
    # jane = Person("Jane", "Smith")
    #
    # print(jane.fullname())
    #
    # print(jane.allowed_titles_starting_with("M"))
    # print(Person.allowed_titles_starting_with("M"))
    #
    # print(jane.allowed_titles_ending_with("s"))
    # print(Person.allowed_titles_ending_with("s"))
