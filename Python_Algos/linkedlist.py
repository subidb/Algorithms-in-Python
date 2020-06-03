import time
import sys


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_start(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            return
        oldhead = self.head
        self.head = newnode
        self.head.next = oldhead
        return

    # @property
    # def completelist(self):
    #     finallist = []
    #     print("\nlinked list current elements(head to tail):")
    #     cursor = self.head
    #     while cursor is not None:
    #         print(cursor.value, end=" ")
    #         cursor = cursor.next

    def print_list(self):
        print("\nlinked list current elements(head to tail):")
        cursor = self.head
        while cursor is not None:
            print(cursor.value, end=" ")
            cursor = cursor.next
            # time.sleep(.5)

    def search(self, value):
        cursor = self.head
        while cursor is not None and cursor.value != value:
            cursor = cursor.next
        return cursor


    def add_middle(self, value, newval):
        point = self.search(value)
        newnode = Node(newval)
        newnode.next = point.next
        point.next = newnode


    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    # def reverse_list(self):
    #     prev = None
    #     cursor = self.head
    #     while cursor is not None:
    #         next = cursor.next
    #         cursor.next = prev
    #         prev = cursor
    #         cursor = next
    #     self.head = prev

        # self.head = cursor




    def __repr__(self):
        return ""


# l1 = LinkedList()
# print(l1)
# l1.insert_start(1)
#
# print(l1.head.value)
l1 = LinkedList()
print(l1.head)

for i in reversed(range(5, 10)):
    print("adding", i)
    l1.insert_start(i)
    print("head = ", l1.head.value)
    print(l1.head)

print()
l1.print_list()

print()
# x1 = l1.head
# print(x1.value)

print(l1.search(6))

l1.add_middle(7, 89)
print("xx")
l1.print_list()
print("x")

# print("\nreversing:")
l1.reverse_list()
l1.print_list()
print()


# print("\n size of int = ", sys.getsizeof(int()))
# print("\n")
# for i in range(5):
#     print(i, end=" ")
#     print(hex(id(i)))
#     print(id(i))



# print(sys.getsizeof(l1.head))










# x = 1
# y = 1
# print(y/2 * 2)
# print(x == y/2 * 2)
# print(x is y/2 * 2)
