queue = []

while True:

    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Front")
    print("4.Rear")
    print("5.Display")
    print("6.Size")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        queue.append(value)

    elif choice == 2:

        if len(queue) == 0:
            print("Queue Empty")
        else:
            print("Removed:", queue.pop(0))

    elif choice == 3:

        if len(queue) == 0:
            print("Queue Empty")
        else:
            print("Front:", queue[0])

    elif choice == 4:

        if len(queue) == 0:
            print("Queue Empty")
        else:
            print("Rear:", queue[-1])

    elif choice == 5:
        print(queue)

    elif choice == 6:
        print(len(queue))

    elif choice == 7:
        break

    else:
        print("Invalid choice")