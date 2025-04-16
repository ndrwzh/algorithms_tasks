class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(left: TreeNode, right: TreeNode) -> int:

    if left is None or right is None:
        return 0
    
    count = 0

    if left.val == right.val:
        count = 1
    
 
    count += dfs(left.left, right.right)
    count += dfs(left.right, right.left)
    
    return count

def count_mirror_twins(root: TreeNode) -> int:

    if root is None:
        return 0
    return dfs(root.left, root.right)