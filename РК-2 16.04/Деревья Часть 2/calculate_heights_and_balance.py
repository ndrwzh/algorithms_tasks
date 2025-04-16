class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0  

def calculate_heights_and_balance(node):
    
    if not node:
        return 0  
    
    
    left_height = calculate_heights_and_balance(node.left)
    right_height = calculate_heights_and_balance(node.right)
    
    node.balance_factor = left_height - right_height
    
    return 1 + max(left_height, right_height)

