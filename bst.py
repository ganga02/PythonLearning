class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert
def insert(root, value):

    if root == None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root


# Search
def search(root, value):

    if root == None:
        return False

    if root.data == value:
        return True

    elif value < root.data:
        return search(root.left, value)

    else:
        return search(root.right, value)


# Traversals
def inorder(root):

    if root == None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):

    if root == None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):

    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")tb


# Min node
def min_value_node(root):

    current = root

    while current.left != None:
        current = current.left

    return current


# Max node
def max_value_node(root):

    current = root

    while current.right != None:
        current = current.right

    return current


# Delete node
def delete(root, value):

    if root == None:
        return root

    if value < root.data:
        root.left = delete(root.left, value)

    elif value > root.data:
        root.right = delete(root.right, value)

    else:

        # No child
        if root.left == None and root.right == None:
            return None

        # One child
        elif root.left == None:
            return root.right

        elif root.right == None:
            return root.left

        # Two children
        temp = min_value_node(root.right)

        root.data = temp.data

        root.right = delete(root.right, temp.data)

    return root


# Update
def update(root, old_value, new_value):

    if search(root, old_value):

        root = delete(root, old_value)

        root = insert(root, new_value)

        print("Updated Successfully")

    else:
        print("Value Not Found")

    return root


# Height of tree
def height(root):

    if root == None:
        return 0

    left_height = height(root.left)

    right_height = height(root.right)

    return max(left_height, right_height) + 1


# Check BST
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):

    if root == None:
        return True

    if root.data <= min_val or root.data >= max_val:
        return False

    return (is_bst(root.left, min_val, root.data) and
            is_bst(root.right, root.data, max_val))


# Delete leaf node only
def delete_leaf(root, value):

    if root == None:
        return root

    if value < root.data:
        root.left = delete_leaf(root.left, value)

    elif value > root.data:
        root.right = delete_leaf(root.right, value)

    else:

        if root.left == None and root.right == None:
            return None

        else:
            print("Not a Leaf Node")

    return root

# Copy Tree
def copy_tree(root):

    if root == None:
        return None

    new_node = Node(root.data)

    new_node.left = copy_tree(root.left)

    new_node.right = copy_tree(root.right)

    return new_node

root = None

while True:

    print("\n1.Insert")
    print("2.Delete")
    print("3.Update")
    print("4.Search")
    print("5.Inorder Traversal")
    print("6.Preorder Traversal")
    print("7.Postorder Traversal")
    print("8.Check isBST")
    print("9.Delete Leaf Node")
    print("10.Min Value Node")
    print("11.Max Value Node")
    print("12.Height of Tree")
    print("13.Copy Tree")
    print("14.Exit")

    choice = int(input("Enter choice: "))

    # Insert
    if choice == 1:

        n = int(input("Enter total number of nodes: "))

        for i in range(n):
            value = int(input("Enter the node value: "))
            root = insert(root,value)

    # Delete
    elif choice == 2:

        value = int(input("Enter value to delete: "))

        root = delete(root, value)

    # Update
    elif choice == 3:

        old_value = int(input("Enter old value: "))
        new_value = int(input("Enter new value: "))

        root = update(root, old_value, new_value)

    # Search
    elif choice == 4:

        value = int(input("Enter value to search: "))

        if search(root, value):
            print("Value Found")
        else:
            print("Value Not Found")

    # Inorder
    elif choice == 5:

        inorder(root)
        print()

    # Preorder
    elif choice == 6:

        preorder(root)
        print()

    # Postorder
    elif choice == 7:

        postorder(root)
        print()

    # Check BST
    elif choice == 8:

        if is_bst(root):
            print("Valid BST")
        else:
            print("Not BST")

    # Delete leaf node
    elif choice == 9:

        value = int(input("Enter leaf node value: "))

        root = delete_leaf(root, value)

    # Min node
    elif choice == 10:

        if root == None:
            print("Tree Empty")
        else:
            print("Min Value =", min_value_node(root).data)

    # Max node
    elif choice == 11:

        if root == None:
            print("Tree Empty")
        else:
            print("Max Value =", max_value_node(root).data)

    # Height
    elif choice == 12:

        print("Height =", height(root))
    # Copy Tree
    elif choice == 13:

        if root == None:
            print("Tree Empty")

        else:
            copied_root = copy_tree(root)

            print("Original Tree (Inorder): ", end="")
            inorder(root)

            print("\nCopied Tree (Inorder): ", end="")
            inorder(copied_root)

            print("\nTree Copied Successfully")  
    # Exit
    elif choice == 14:
        break

    else:
        print("Invalid Choice")