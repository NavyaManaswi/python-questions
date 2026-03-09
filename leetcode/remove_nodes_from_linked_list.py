class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

# def del_nodes(head):
#     if head is None or head.next is None:
#         return head
#     temp = head
#     while temp is not None and temp.next is not None:
#         if temp.data < temp.next.data:
#             temp.next= temp.next.next
#             # temp = None
#         else:    
#             temp = temp.next
#     return head

def reverse(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    return prev


def del_nodes(head):
    if head is None or head.next is None:
        return head
    head = reverse(head)
    max_val = head.data
    curr = head
    while curr and curr.next:
        if curr.next.data < max_val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            max_val = curr.data
    head = reverse(head)

    return head

def print_value(head):
    temp = head
    while temp is not None:
        print(f"{temp.data}", end= "-->") 
        temp = temp.next      
    print("None")

if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next= Node(5)
    head.next.next.next= Node(10)
    print_value(head)
    final= del_nodes(head)
    print_value(final)     