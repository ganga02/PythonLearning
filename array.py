arr=[]
while(True):
    print("\n1.Insert")
    print("\n2.Display")
    print("\n3.Delete")
    print("\n4.Search")
    print("\n5.Min Value")
    print("\n6.Max Value")
    print("\n7.Reverse")
    print("\n8.Sort")
    print("\n9.Exit")

    choice = int(input("Enter the choice:"))
    if choice == 1:
        value = int(input("Enter the value to insert: "))
        arr.append(value)
    elif choice == 2:
        print(arr)
    elif choice == 3:
        value = int(input("Enter the value to delete: "))
        if value in arr:
            arr.remove(value)
        else:
            print("Element not found")
    elif choice == 4:
        value = int(input("Enter the value to search: "))
        if value in arr:
            print("Value Found")
        else:
            print("Value not Found")
    elif choice == 5:
        print(min(arr))
    elif choice == 6:
        print(max(arr))
    elif choice == 7:
        arr.reverse()
        print(arr)
    elif choice == 8:
        arr.sort()
        print(arr)
    elif choice == 9:
        break
    else:
        print("Invalid choice")
