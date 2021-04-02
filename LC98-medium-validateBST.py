# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return true
        
        lower = float('-inf')
        upper = float('inf')
        
        return self.checkNode(root, lower, upper)
        
        
    def checkNode(self, node, lower, upper):
        if not node:
            return True
        
        isValidNode = node.val > lower and node.val < upper
        if not isValidNode:
            return False
        
        isValidLeft = self.checkNode(node.left, lower, node.val)
        if not isValidLeft:
            return False
        
        return self.checkNode(node.right, node.val, upper)