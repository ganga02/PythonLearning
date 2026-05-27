stack = []

while True:

    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Size")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)

    elif choice == 2:

        if len(stack) == 0:
            print("Stack Empty")
        else:
            print("Removed:", stack.pop())

    elif choice == 3:

        if len(stack) == 0:
            print("Stack Empty")
        else:
            print("Top:", stack[-1])

    elif choice == 4:
        print(stack)

    elif choice == 5:
        print(len(stack))

    elif choice == 6:
        break

    else:
        print("Invalid choice")