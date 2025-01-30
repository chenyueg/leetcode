"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root: 
            return []
        
        stack = [root]
        out = []
        
        while len(stack):
            top = stack.pop()
            out.append(top.val)
            stack.extend(top.children or [])
        
        return out[::-1]