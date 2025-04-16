from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_complete_tree(root):
    
    if not root:
        return True
    
    queue = deque([root])
    seen_null = False
    
    while queue:
        node = queue.popleft()
        
        if not node:
            seen_null = True
        else:
            
            if seen_null:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
    
    return True