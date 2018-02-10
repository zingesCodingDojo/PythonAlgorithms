
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
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
            print("Error: 'Get index is out of range!")
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
            print("Error: 'Index is out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                print("Success")
                return True
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
        if self.head is not None:
            temp = self.head.next
            del self.head
            self.head = temp
            print("There was a head")
            return True
        print("Error: No head to remove")
        return False


my_list = SLL()
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

print("Element at 2nd index: %d" % my_list.get(2))

my_list.find_m_to_last_element(5)

my_list.remove_head()
my_list.display()



class SpecialNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False  # Do not allow duplicates in tree!
        elif self.data > data:  # Is value less than?
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = SpecialNode(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = SpecialNode(data)
                return True

    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False  # No further nodes in left side of tree to find!
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False  # No further nodes in right side of the tree!

    def preorder(self):
        if self:
            print(str(self.data))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data))
            if self.rightChild:
                self.rightChild.inorder()


class BeautifulTree:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head:
            return self.head.insert(data)
        else:
            self.head = SpecialNode(data)

    def find(self, data):
        if self.head:
            return self.head.find(data)
        else:
            return False  # Data not in tree

    def preorder(self):
        print("PreOrder")
        self.head.preorder()

    def postorder(self):
        print("PostOrder")
        self.head.postorder()

    def inorder(self):
        print("InOrder")
        self.head.inorder()


myBST = BeautifulTree()
myBST.insert(10)
print(myBST.insert(15))
myBST.insert(14)
myBST.preorder()
myBST.postorder()
myBST.inorder()
