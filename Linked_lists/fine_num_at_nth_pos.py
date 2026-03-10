class Node:
    def __init__(self, data):
        self.data = data
        self.next= None

def reverse(head):
    curr = head
    prev= None
    while curr is not None:
        next_node= curr.next
        curr.next= prev
        prev= curr
        curr = next_node
    return prev

def find_node(head,pos):
    head= reverse(head)
    temp = head
    count = 1
    while temp is not None:
        if count == pos:
            print(temp.data)
        count = count+1  
        temp = temp.next  

if __name__ == "__main__":
    head= Node(35)
    head.next = Node(15)
    head.next.next = Node(4)
    head.next.next.next=Node(20)
    pos=4
    find_node(head, pos)             