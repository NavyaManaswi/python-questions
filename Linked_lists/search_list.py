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
    print("None") 
    print(cur)

def search_key(head, value):
    temp = head
    while temp is not None:
        if temp.data == value:
            return True
        temp = temp.next    
                       
if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(10)
    print_value(head)
    key= 20
    if search_key(head, key):
        print("True")
    else:
        print("False")    
