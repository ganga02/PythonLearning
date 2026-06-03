class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):

    if root == None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root


def min_value_node(root):

    current = root

    while current.left != None:
        current = current.left

    return current


def delete(root, value):

    if root == None:
        return root

    # Go left
    if value < root.data:
        root.left = delete(root.left, value)

    # Go right
    elif value > root.data:
        root.right = delete(root.right, value)

    # Node found
    else:

        # Case 1: No child (leaf node)
        if root.left == None and root.right == None:
            return None

        # Case 2: One child
        elif root.left == None:
            return root.right

        elif root.right == None:
            return root.left

        # Case 3: Two children
        temp = min_value_node(root.right)

        root.data = temp.data

        root.right = delete(root.right, temp.data)

    return root


root = None

n = int(input("Enter number of nodes: "))

for i in range(n):

    value = int(input("Enter value: "))
    root = insert(root, value)


delete_value = int(input("Enter value to delete: "))

root = delete(root, delete_value)