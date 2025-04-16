class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#функция для проверки идентичности деревьев
def is_same_tree(a: TreeNode, b: TreeNode) -> bool:
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.val == b.val and is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

def is_subtree(A: TreeNode, B: TreeNode) -> bool:
    
    
    if not B:
        return True
    if not A:
        return False
  
    if is_same_tree(A, B):
        return True
    
    return is_subtree(A.left, B) or is_subtree(A.right, B)