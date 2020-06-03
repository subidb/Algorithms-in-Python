def preorder_traversal(node):
    if node is None:
        return
    print(node.key, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=" ")


def recursive_search(root, value):
    x = root
    if x is None or x.key == value:
        return x
    if value > x.key:
        return recursive_search(x.right, value)
    else:
        return recursive_search(x.left, value)


def itr_search(root, value):
    x = root
    while x is not None and x.key != value:
        if value > x.key:
            x = x.right
        else:
            x = x.left
    return x



if __name__ == "__main__":
    print("x")