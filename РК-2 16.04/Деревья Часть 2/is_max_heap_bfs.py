class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_max_heap_bfs(root):

    if not root:
        return True
    
    from collections import deque
    queue = deque([root])
    should_be_leaf = False
    
    while queue:
        current = queue.popleft()
        
        if current.left:
            if should_be_leaf or current.left.val > current.val:
                return False
            queue.append(current.left)
        else:
            should_be_leaf = True
        

        if current.right:
            if should_be_leaf or current.right.val > current.val:
                return False
            queue.append(current.right)
        else:
            should_be_leaf = True
    
    return True