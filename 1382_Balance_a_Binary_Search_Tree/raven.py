# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorder(self, node, arr):
    if not node: return
    self.inorder(node.left, arr)
    arr.append(node)
    self.inorder(node.right, arr)
    
  def generate(self, arr):
    if len(arr) == 0:
      return None
    mid = len(arr) // 2
    arr[mid].left = self.generate(arr[:mid])
    arr[mid].right = self.generate(arr[mid + 1:])
    return arr[mid]
  
  def balanceBST(self, root: TreeNode) -> TreeNode:
    arr = [] 
    self.inorder(root, arr)
    res = self.generate(arr)
    return res
    
