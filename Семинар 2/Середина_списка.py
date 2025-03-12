class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

