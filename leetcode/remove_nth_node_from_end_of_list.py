class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

def reverse(head):
    if head is None or head.next is None:
        return head
    temp = head
    prev= None
    while temp is not None:
        next_node= temp.next
        temp.next= prev
        prev= temp
        temp = next_node
    return prev
def delete_at_any_pos(head,pos):
    head= reverse(head)
    temp = head
    if pos==1:
        head= head.next
        resp = reverse(head)
        return resp
    else:
        prev= None
        for i in range(1, pos):
            prev = temp
            temp = temp.next
        prev.next = temp.next
    resp= reverse(head)
    return resp

def print_value(head):
    temp = head
    while temp is not None:
        print(f"{temp.data}", end = "-->")
        temp = temp.next
    print("Done")

if __name__ == "__main__":
    head= Node(1)      
    head.next= Node(2)
    head.next.next= Node(3)
    print_value(head)    
    pos= 1
    # print_value(reverse(head))
    final= delete_at_any_pos(head,pos)
    print_value(final) 