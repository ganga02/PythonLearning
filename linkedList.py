class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
head = None
while True:
    print("\n1.Insert at Begining")
    print("2.Insert at End")
    print("3.Delete at Begining")
    print("4.Delete at End")
    print("5.Update")
    print("6.Search")
    print("7.Display")
    print("8.Exit")
    
    choice = int(input("Enter the choice: "))
    if choice == 1:
        value = int(input("Enter the value to insert: "))
        new_Node = Node(value)
        if head == None:
            head = new_Node
        else:
            new_Node.next = head
            head = new_Node
    elif choice == 2:
        value = int(input("Enter the value to insert: "))
        new_Node = Node(value)
        if head == None:
            head = new_Node
        elif head.next == None:
            head.next = new_Node
        else:
            current = head
            while current.next != None:
                current=current.next
            current.next = new_Node
    elif choice == 3:
        if head == None:
            print("LinkedList if Empty")

        else:
            head = head.next

    elif choice == 4:
        if head == None:
            print("Linked List is Empty")
        elif head.next == None:
            head = None
        else:
            current = head
            while current.next.next !=None:
                current = current.next
            current.next = None
    elif choice == 5:
        if head == None:
            print("Linked List is Empty")
        else:
            old_Value = int(input("Enter the value to update: "))
            new_Value = int(input("Enter the new value: "))
            current = head
            found = False
            while current!=None:
                if current.value == old_Value:
                    current.value = new_Value
                   
                    found = True
                    break
                current=current.next
            if found:
                print("Updated Successfully")
            else:
                print("Value not Found")
    elif choice == 6:
        if head == None:
            print("Linked List is Empty")
        else:
            search_Value = int(input("Enter the value to search: "))
            
            current = head
            found = False
            while current!=None:
                if current.value == search_Value:
                    
                    found = True
                    break
                current=current.next
            if found:
                print("Value Found")
            else:
                print("Value not Found")
    elif choice == 7:
        if head == None:
            print("Linked List is empty")
        else:
            current = head
            while current!=None:
                print(current.value, end="->")
                current=current.next
            print("None")
    elif choice ==8:
        break
    else:
        print("Invalid Choice")
        
                




        

    
