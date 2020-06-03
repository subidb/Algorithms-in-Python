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

    @property
    def treeroot(self):
        return self.root


    def insert(self, values):  # values is a list
        for value in values:
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
            else:
                if newnode.key >= y.key:
                    y.right = newnode
                else:
                    y.left = newnode


    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent


    def tree_max(self, node=None):
        cursor = node
        if cursor is None:
            cursor = self.root
        while cursor is not None:
            node = cursor
            cursor = cursor.right
        return node


    def tree_min(self, node=None):
        cursor = node
        if cursor is None:
            cursor = self.root
        while cursor.left is not None:
            cursor = cursor.left
        return cursor

    def itr_search(self, value):
        cursor = self.root
        while cursor.key != value and cursor is not None:
            if value > cursor.key:
                cursor = cursor.right
            else:
                cursor = cursor.left
        return cursor


    def recur_search(self, node, value):
        cursor = node
        if cursor.key == value or cursor is None:
            return cursor
        if value >= cursor.key:
            return self.recur_search(cursor.right, value)
        else:
            return self.recur_search(cursor.left, value)



    def find_successor(self, node):
        cursor = node
        if cursor.right is not None:
            return self.tree_min(cursor.right)
        p = cursor.parent
        while p is not None and cursor != p.left:
            cursor = p
            p = p.parent
        return p


    def delete(self, node):

        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            suc = self.tree_min(node.right)
            # suc = self.find_successor(node)
            if suc.parent != node:
                self.transplant(suc, suc.right)
                suc.right = node.right
                suc.right.parent = suc
            self.transplant(node, suc)
            suc.left = node.left
            node.left.parent = node






tree1 = Tree()
tree1.insert([10, 1, 3])
tree1.insert([5, 4, 15, 6, 11, 20])

print("\npre order:")
traversals.preorder_traversal(tree1.root)  # 10, 1, 3, 5, 4, 6, 15, 11, 20
print()
# traversals.inorder_traversal(tree1.root)
# print()
# traversals.postorder_traversal(tree1.root)

print("min from {}, = ".format(tree1.itr_search(5).key), tree1.tree_min(tree1.itr_search(5)).key)
print("max = ", tree1.tree_max().key)

print("search = ", tree1.recur_search(tree1.root, 20).key)

x = 11
print("successor of {} = ".format(tree1.itr_search(x).key), tree1.find_successor(tree1.itr_search(x)).key)


tree1.insert([2])
print("\npre order: ")
traversals.preorder_traversal(tree1.root)


print()
node_del = 5
print("\ndeleting: {}".format(node_del), tree1.delete(tree1.itr_search(node_del)))

# tree1.transplant(tree1.itr_search(3), tree1.itr_search(5))
traversals.preorder_traversal(tree1.root)
#
# print("\n")
# print(tree1.root.left.right.left.parent.key)

