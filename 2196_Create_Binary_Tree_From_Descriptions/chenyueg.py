# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        child_nodes = set()

        for desc in descriptions:
            parent_val, child_val, is_left = desc

            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)

            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)

            if is_left:
                node_map[parent_val].left = node_map[child_val]
            else:
                node_map[parent_val].right = node_map[child_val]

            child_nodes.add(child_val)

        for desc in descriptions:
            parent_val = desc[0]

            if parent_val not in child_nodes:
                return node_map[parent_val]

        return None