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


def inorder(root):

    if root == None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


root = None

n = int(input("Enter number of strings: "))

for i in range(n):

    word = input("Enter word: ")

    root = insert(root, word)

print("Sorted words:")
inorder(root)