class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  
        curr.next = prev       
        prev = curr            
        curr = next_node       
    return prev  



