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

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, current_node):
        if data == current_node.data:
            return current_node
        elif data < current_node.data and current_node.left_child is not None:
            return self._find(data, current_node.left_child)
        elif data > current_node.data and current_node.right_child is not None:
            return self._find(data, current_node.right_child)

    def delete_data(self, data):
        return self.delete_node(self.find(data))

    def delete_node(self, node):
        # returns the node with min data in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def number_children(n):
            num_children = 0
            if n.left_child is not None:
                num_children += 1
            if n.right_child is not None:
                num_children += 1
            return num_children

        # get the paretnt of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = number_children(node)

        # break operation into different cases based on the structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly holding the data we wished to delete
            node.data = successor.data

            # delete the inorder successor now that it's data was copied into the other node
            self.delete_node(successor)


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

ree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(11)

tree.print_tree()
print("About to delete 5!")
tree.delete_data(5)
tree.print_tree()
print("About to delete 4!")
tree.delete_data(4)
tree.print_tree()