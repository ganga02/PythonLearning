
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    arr.append(value)

while True:

    print("\n1. Traversal")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at any position")
    print("5. Delete at beginning")
    print("6. Delete at end")
    print("7. Delete at any position")
    print("8. Update at any position")
    print("9. Search")
    print("10. Reverse array")
    print("11. Find max/min")
    print("12. Remove duplicates")
    print("13. Merge arrays")
    print("14. Rotate array")
    print("15. Frequency count")
    print("16. Exit")

    choice = int(input("Enter choice: "))

    # 1. Traversal
    if choice == 1:

        if len(arr) == 0:
            print("Array is empty")
        else:
            print(arr)

    # 2. Insert at beginning
    elif choice == 2:

        value = int(input("Enter value: "))

        arr.insert(0, value)

        print(arr)

    # 3. Insert at end
    elif choice == 3:

        value = int(input("Enter value: "))

        arr.append(value)

        print(arr)

    # 4. Insert at any position
    elif choice == 4:

        position = int(input("Enter position: "))
        value = int(input("Enter value: "))

        if position >= 0 and position <= len(arr):

            arr.insert(position, value)

            print(arr)

        else:
            print("Invalid position")

    # 5. Delete at beginning
    elif choice == 5:

        if len(arr) == 0:
            print("Array is empty")

        else:
            arr.pop(0)

            print(arr)

    # 6. Delete at end
    elif choice == 6:

        if len(arr) == 0:
            print("Array is empty")

        else:
            arr.pop()

            print(arr)

    # 7. Delete at any position
    elif choice == 7:

        position = int(input("Enter position: "))

        if position >= 0 and position < len(arr):

            arr.pop(position)

            print(arr)

        else:
            print("Invalid position")

    # 8. Update at any position
    elif choice == 8:

        position = int(input("Enter position: "))
        value = int(input("Enter new value: "))

        if position >= 0 and position < len(arr):

            arr[position] = value

            print(arr)

        else:
            print("Invalid position")

    # 9. Search
    elif choice == 9:

        value = int(input("Enter value to search: "))

        found = False

        for i in range(len(arr)):

            if arr[i] == value:

                print("Value found at index", i)

                found = True

                break

        if found == False:
            print("Value not found")

    # 10. Reverse array
    elif choice == 10:

        arr.reverse()

        print(arr)

    # 11. Find max/min
    elif choice == 11:

        if len(arr) == 0:
            print("Array is empty")

        else:
            print("Maximum =", max(arr))
            print("Minimum =", min(arr))

    # 12. Remove duplicates
    elif choice == 12:

        new_arr = []

        for value in arr:

            if value not in new_arr:
                new_arr.append(value)

        arr = new_arr

        print(arr)

    # 13. Merge arrays
    elif choice == 13:

        second_arr = []

        n = int(input("Enter size of second array: "))

        for i in range(n):

            value = int(input("Enter value: "))
            second_arr.append(value)

        merged_array = arr + second_arr

        print("Merged array =", merged_array)

    # 14. Rotate array
    elif choice == 14:

        k = int(input("Enter number of rotations: "))

        if len(arr) == 0:
            print("Array is empty")

        else:
            k = k % len(arr)

            arr = arr[-k:] + arr[:-k]

            print(arr)

    # 15. Frequency count
    elif choice == 15:

        frequency = {}

        for value in arr:

            if value in frequency:
                frequency[value] += 1

            else:
                frequency[value] = 1

        print(frequency)

    # Exit
    elif choice == 16:

        break

    else:
        print("Invalid choice")


