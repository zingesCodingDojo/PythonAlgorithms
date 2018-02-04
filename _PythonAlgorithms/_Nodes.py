

"""
This will contain all node types for algorithm classes.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class BTSNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
