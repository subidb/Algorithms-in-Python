import traversals


class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        print("inserting: ", value)
        newnode = Node(value)
        y = None
        x = self.root
        while x is not None:
            y = x
            if newnode.key > x.key:
                x = x.right
            else:
                x = x.left

        newnode.parent = y
        if y is None:
            self.root = newnode
            return
        if newnode.key >= y.key:
            y.right = newnode
        else:
            y.left = newnode


    def preorder_traversal(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=" ")


    # def inorder_traversal
    # # @staticmethod
    # def return_val(self, node):
    #     if node is None:
    #         return None
    #     return node.key


t = Tree()
# print(t.key)

t.insert(10)
# print(t.root.key)
t.insert(5)
t.insert(15)
t.insert(11)
t.insert(8)


# print(t.root.right.left.key)
#
print("pre order: \n")
t.preorder_traversal(t.root.right)
print()
t.inorder_traversal(t.root)
print()
t.postorder_traversal(t.root)
print()

traversals.preorder_traversal(t.root)
# print(t.return_val(t.root))
v = int(input("\n\nnumber to search: "))

# node = traversals.recursive_search(t.root, x)
node = traversals.itr_search(t.root, v)
if node:
    print(node.key)
else:
    print("not found")


