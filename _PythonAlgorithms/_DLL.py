from _Nodes import OtherDLLNode as node
from _Nodes import DLLNode

"""
This is the Doubly Linked List Class.
We will be able to add, remove, edit, traverse both forwards and backwards, and check for circular movements.
"""


class DLL:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head

        if current.prev is not None:
            current.prev(new_node)

        while current.next is not None:
            current = current.next

        new_node.prev = current.next
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

            print("My current value is %s and my next value is gonna be..." % current_node.data)

            current_node = current_node.next

            print("Now my current value is... %s" % current_node.data)

            elements.append(current_node.data)

        while current_node.prev is not None:

            print("My current value is at %s and my previous value is gonna be..." % current_node.data)

            current_node = current_node.prev

            print("Now my current value is... %s" % current_node.data)

        print elements


# my_list = DLL()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# my_list.display()



def multipliers():
    return [lambda x: i * x for i in range(4)]


print [m(2) for m in multipliers()]

my_string = "Hello World"
print ''.join(reversed(my_string))

# class SingletonDecorator:
#     def __init__(self,klass):
#         self.klass = klass
#         self.instance = None
#     def __call__(self,*args,**kwds):
#         if self.instance == None:
#             self.instance = self.klass(*args,**kwds)
#         return self.instance
#
# class foo: pass
# foo = SingletonDecorator(foo)
#
# x=foo()
# y=foo()
# z=foo()
# x.val = 'sausage'
# y.val = 'eggs'
# z.val = 'spam'
# print(x.val)
# print(y.val)
# print(z.val)
# print(x is y is z)


class SecondDLL(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def append(self, data):
        new_node = DLLNode(data, self.head)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node
        self.size += 1

    def erase(self, data):
        current_node = self.head

        while current_node:
            if current_node.get_data() == data:
                _next = current_node.get_next()
                _prev = current_node.get_prev()

                if _next:
                    _next.set_prev(_prev)
                if _prev:
                    _prev.set_next(_next)
                else:
                    self.head = current_node

                self.size -= 1
                return True  # data was removed!
            else:
                current_node = current_node.get_next()
        return False  # data not found!

    def search(self, data):
        current_node = self.head

        while current_node:
            if current_node.get_data() == data:
                return data
            else:
                current_node = current_node.get_next()

        return None


"""
This is the Circular Linked List Class.
We will be able to add, remove, edit, traverse.
"""