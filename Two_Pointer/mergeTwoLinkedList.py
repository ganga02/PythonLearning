class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_linkedList(arr):
    head=Node(arr[0])
    current=head
    for i in range(1,len(arr)):
        current.next=Node(arr[i])
        current=current.next
    return head
 
def merge_linkedList(list1,list2):
    dummy=Node(0)
    current=dummy
    while list1 and list2:
        if list1.data < list2.data:
            current.next=list1
            list1=list1.next
        else:
            current.next=list2
            list2=list2.next
        current=current.next
    if list1:
        current.next=list1
        list1=list1.next
        
    if list2:
        current.next=list2
        list2=list2.next
        
    return dummy.next

def print_arr(head):
    result=[]
    current=head
    while current!=None:
        result.append(current.data)
        current=current.next
    print(result)
    
    
    
arr1=[1,2,4]
arr2=[1,3,4]
list1=create_linkedList(arr1)
list2=create_linkedList(arr2)
merged=merge_linkedList(list1,list2)
print_arr(merged)