class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

def delete_at_end(head):
    if head is None:
        return None

    if head.next is None:
        return head

    temp = head
    if temp.next.next is not None:
        temp = temp.next
    temp.next= None
    return head      

def print_value(head):
    temp = head
    while temp is not None:
        print(f"{temp.data}",end="-->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next = Node(30)
    print_value(head)
    final = delete_at_end(head)
    print_value(final)              