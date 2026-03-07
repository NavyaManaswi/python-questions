class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

def print_value(new_Data):
    temp= new_Data
    cur= 0
    while temp is not None:
        print(f"{temp.data}", end ="--->")
        cur = cur +1
        temp = temp.next
    print("None") 
    print(cur) 
        
def insert_at_front(head, val):
    newnode= Node(val)
    newnode.next= head
    return newnode
        
if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(10)
    print_value(head)
    key= 20
    if search_key(head, key):
        print("True")
    else:
        print("False")    
    val= 40
    front= insert_at_front(head,val)
    print_value(front)    
    val2=100
    last= insert_at_end(head, val2)
    print_value(last)
