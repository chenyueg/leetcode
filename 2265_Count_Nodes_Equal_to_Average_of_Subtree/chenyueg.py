# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def subtreeSum(self, curr):
        if curr is None:
            return 0, 0

        leftSubtree = self.subtreeSum(curr.left)
        rightSubtree = self.subtreeSum(curr.right)

        sum = leftSubtree[0] + rightSubtree[0] + curr.val
        num = leftSubtree[1] + rightSubtree[1] + 1

        if sum // num == curr.val:
           self.count += 1
        
        return sum, num

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.subtreeSum(root)
        return self.count