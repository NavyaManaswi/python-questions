class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

def delete_first_node(head):
    temp= head
    head= head.next
    temp=None
    return head

def print_value(head):
    temp= head
    while temp is not None:
        print(temp.data, end="-->")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20) 
    head.next.next = Node(30)
    print_value(head)
    final = delete_first_node(head)
    print_value(final)      