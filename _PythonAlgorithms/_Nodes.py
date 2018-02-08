

"""
This will contain all node types for algorithm classes.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class DLLNode:
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next = next_node
        self.previous_node = previous_node

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def get_prev(self):
        return self.previous_node

    def set_prev(self, previous_node):
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class OtherDLLNode:
    def __init__(self, data=None, ):
        self.data = data
        self.next = None
        self.prev = None


class BTSNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
