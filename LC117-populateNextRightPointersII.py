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
        leftMost = root
        isLeftTaken = False
        
        child1, currNode, isLeftTaken = self.findGoodChild(currNode, isLeftTaken)
        
        while True:           
            if not child1:
                leftMost = self.findLeftMost(leftMost)
                if not leftMost:
                    break
                child1, currNode, isLeftTaken = self.findGoodChild(leftMost, False)
                continue
                
            child2, currNode, isLeftTaken = self.findGoodChild(currNode, isLeftTaken)
            
            if not child2:
                leftMost = self.findLeftMost(leftMost)
                if not leftMost:
                    break
                child1, currNode, isLeftTaken = self.findGoodChild(leftMost, False)
                continue
                
            child1.next = child2
            child1 = child2
            
        return root
            
            
    def findChild(self, node, isLeftTaken):
        if not node:
            return None, None, False
        
        if node.left and not isLeftTaken:
            return node.left, node, True
        
        return node.right, node.next, False
        
    def findGoodChild(self, node, isLeftTaken):
        currNode = node
        
        while True:
            if not currNode:
                return None, None, False
            
            childNode, nextNode, isLeftTaken = self.findChild(currNode, isLeftTaken)
            
            if childNode:
                return childNode, nextNode, isLeftTaken
            
            currNode = nextNode
            
    def findLeftMost(self, leftMost):
        if not leftMost:
            return None
            
        while True:
            leftMost, nextNode, _ = self.findGoodChild(leftMost, False)

            if leftMost:
                return leftMost
            
            if not nextNode:
                return None
               
            
            
        
        
        
        
        