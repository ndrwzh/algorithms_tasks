class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, val):
    if head is None:
        return None
    if head.data == val:
        return head.next
    current = head
    while current.next:
        if current.next.data == val:
            current.next = current.next.next
            return head  
        current = current.next
    return head  
