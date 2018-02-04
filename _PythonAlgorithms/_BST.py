from _Nodes import BTSNode as node
from random import randint


class BTS:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left_child is None:
                current_node.left_child = node(data)
            # Use recursion to find the empty left leaf node.
            else:
                self._insert(data, current_node.left_child)

        elif data > current_node.data:
            # another outer case
            # when larger
                if current_node.right_child is None:
                    current_node.right_child = node(data)
                else:
                    self._insert(data, current_node.right_child)

        else:
            print("Data already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(str(current_node.data))
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.data:
            return True
        elif value < current_node.data and current_node.left_child is not None:
            return self._search(value, current_node.left_child)
        elif value > current_node.data and current_node.right_child is not None:
            return self._search(value, current_node.right_child)
        return False


def fill_tree(tree, num_elems=100, max_int=1000):
    for _ in range(num_elems):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree


tree = BTS()
# tree = fill_tree(tree)

tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)

tree.print_tree()

print("Tree height: " + str(tree.height()))

print(tree.search(10))
print(tree.search(30))
