class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_at_any_pos(head,pos):
    temp = head
    if pos==1:
        head= head.next
        return head
    prev= None
    for i in range(1, pos):
        prev = temp
        temp = temp.next
    prev.next = temp.next
    return head

def delete_value(head, value):
    while head and head.data == value:
        head = head.next
    temp = head
    prev= None
    while temp:
        if temp.data == value:
            prev.next= temp.next
            temp = temp.next
        else:
            prev= temp
            temp = temp.next 
    return head           

def print_value(head):
    temp = head
    while temp is not None:
        print(f"{temp.data}",end="-->")
        temp = temp.next
    print("None")    

if __name__== "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next = Node(30)
    pos= 30
    final= delete_value(head,pos)
    print_value(final)
    