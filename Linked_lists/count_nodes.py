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
    print("completed") 
    print(cur)
        
if __name__ == "__main__":
    head= Node(10)
    head.next= Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(10)
    print_value(head)