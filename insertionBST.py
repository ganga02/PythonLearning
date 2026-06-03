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


root = None

n = int(input("Enter number of nodes: "))

for i in range(n):

    value = int(input("Enter value: "))

    root = insert(root, value)