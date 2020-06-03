class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def add_start(self, value):
        newnode = Node(value)
        if self.head is not None:
            self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode


    def delete(self, value):
        print("\ndeleting: ", value)
        cursor = self.head
        while cursor is not None and cursor.value != value:
            if cursor.next is None:
                print("not found")
                return
            cursor = cursor.next

        if cursor.prev is not None:
            cursor.prev.next = cursor.next
        else:
            self.head = cursor.next
        if cursor.next is not None:
            cursor.next.prev = cursor.prev


    @property
    def currentlist_values(self):
        curlist = []
        cursor = self.head
        while cursor is not None:
            curlist.append(cursor.value)
            cursor = cursor.next
        return curlist

    def search(self, value):
        cursor = self.head
        while cursor is not None and cursor.value != value:
            cursor = cursor.next
        return cursor

    def print_list(self):
        cursor = self.head
        while cursor is not None:
            print(cursor.value, end=" ")
            cursor = cursor.next

    def print_listreverse(self):
        cursor = self.head
        while cursor.next is not None:
            cursor = cursor.next
        while cursor is not None:
            print(cursor.value, end=" ")
            cursor = cursor.prev

    def list_reverse(self):
        cursor = self.head
        prev = None
        while cursor is not None:
            next = cursor.next
            cursor.next = prev
            cursor.prev = next
            prev = cursor
            cursor = next
        self.head = prev
#



db = DoublyLinkedList()
print(db)

# db.add_start(2)
# print(db.head.value)

for i in range(4, 8):
    db.add_start(i)
    print("x=", i)

print("head.value = ", db.head.value)
# print(db.head.next.value)

print("\nlist = ", db.currentlist_values)
# db.delete(4)
print("listlist = ", db.currentlist_values)


# db.print_list()


# db.print_listreverse()
# print(db.head.next.prev.next.next.next.prev.value)

print("\nreversing list:")
db.list_reverse()


db.print_list()
print()
print("printing list in reverse order(reverse order after reversing the list, so original order:")
db.print_listreverse()

# print(db.head.value)
