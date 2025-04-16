from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetricDFS(root):
    if not root:
        return True
    
    def dfs(node, data):
        if not node:
            data.append(None)
            return
        data.append(node.val)
        dfs(node.left, data)
        dfs(node.right, data)
        return data
    
    data = dfs(root, [])
    j = len(data) - 1
    for i in range(len(data) // 2):
        if data[i] != data[j]:
            return False
        j -= 1
    return True