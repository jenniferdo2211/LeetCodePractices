"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        currNode = root
        leftMostNode = Node(0, root)
        
        while currNode.left:
            leftChild = currNode.left
            rightChild = currNode.right
            leftChild.next = rightChild
            
            if currNode.next:
                leftNext = currNode.next.left
                rightChild.next = leftNext
                currNode = currNode.next
            
            else:
                leftMostNode = leftMostNode.left
                currNode = leftMostNode.left
                
        return root