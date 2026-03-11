class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

def get_node(head):
    slow= head
    fast= head
    prev= None
    while fast is not None and fast.next is not None:
        fast= fast.next.next
        prev= slow
        slow= slow.next
    prev.next= slow.next    
    return head

def print_value(new_Data):
    temp= new_Data
    cur= 0
    while temp is not None:
        print(f"{temp.data}", end ="--->")
        cur = cur +1
        temp = temp.next
    print("completed")    
        
if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(100)
    print_value(head)        
    print_value(get_node(head))    