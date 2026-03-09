class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

def reverse_list(head):
    if head is None or head.next is None:
        return head
    curr= head
    prev=None
    while curr is not None:
        next_node= curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev

def print_value(head):
    temp= head
    while temp is not None:
        print(f"{temp.data}", end="-->")
        temp= temp.next
    print("None")

if __name__ == "__main__":
    head= Node(10)
    head.next=Node(20)
    # head.next.next=Node(30)
    print_value(head)
    final= reverse_list(head)
    print_value(final)                    