# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.equal_count = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.sum_of_sub_tree(root)
        return self.equal_count

    def sum_of_sub_tree(self, root: TreeNode):
        if root == None:
            return 0, 0
        left_sum, left_count = self.sum_of_sub_tree(root.left)
        right_sum, right_count = self.sum_of_sub_tree(root.right)
        current_sum = root.val + left_sum + right_sum
        current_count = left_count + right_count + 1
        if (current_sum) // (current_count) == root.val:
            self.equal_count += 1
        return current_sum, current_count