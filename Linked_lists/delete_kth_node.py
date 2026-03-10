class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

def del_nth_pos(head,pos):
    temp = head
    count = 0
    prev=None
    while temp is not None:
        count = count+1
        if count%pos == 0:
            if prev is not None:
                prev.next= temp.next
            else:
                head= temp.next    
        else:    
            prev= temp
        temp= temp.next  
    return head    

def print_value(head):
    temp= head
    while temp is not None:
        print(f"{temp.data}",end="-->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next = Node(30)
    print_value(head)
    pos= 2
    final = del_nth_pos(head,pos)
    print_value(final)            