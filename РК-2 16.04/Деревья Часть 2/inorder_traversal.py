class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:

    counter = [0]  # Используем список для передачи по ссылке
    result = [None]  # Храним результат
    
    def inorder_traversal(node):
        if not node or result[0] is not None:
            return
        
        
        inorder_traversal(node.left) # Обход левого поддерева
        
        # Увеличиваем счетчик и проверяем текущий узел
        if result[0] is not None:
            return
        
        counter[0] += 1
        if counter[0] == k:
            result[0] = node.val
            return
        
        
        inorder_traversal(node.right) # Обход правого поддерева
    
    inorder_traversal(root)
    return result[0]