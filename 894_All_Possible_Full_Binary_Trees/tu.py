# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        else:
            return [
                TreeNode(0, left = l, right = r)
                for i in range(1, n, 2)
                for l in self.allPossibleFBT(i)
                for r in self.allPossibleFBT(n - i - 1)
            ]
        