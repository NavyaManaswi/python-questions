class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

def find_nth_node(head,pos):
    temp = head
    count =1
    while temp is not None:
        if count == pos:
            return  temp.data
        count = count +1
        temp = temp.next       

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
    pos= 1
    final = find_nth_node(head,pos)
    print(final)            