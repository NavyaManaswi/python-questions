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
    print("completed") 
    print(cur)

def insert_at_end(head, val):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next= Node(val)
    return head
        
        
if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(10)
    print_value(head)
    val2=100
    last= insert_at_end(head, val2)
    print_value(last)
