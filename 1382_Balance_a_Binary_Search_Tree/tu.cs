/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode BalanceBST(TreeNode root) {
        var nodes = new List<int>();
        InorderTraversal(root, nodes);
        return SortedListToBST(nodes, 0, nodes.Count-1);
    }

    private void InorderTraversal(TreeNode root, List<int> nodes)
    {
        if(root==null)
        {
            return;
        }
        InorderTraversal(root.left, nodes);
        nodes.Add(root.val);
        InorderTraversal(root.right, nodes);
    }

    private TreeNode SortedListToBST(List<int> nodes, int start, int end)
    {
        if(start>end)
        {
            return null;
        }
        int mid = start + (end-start) / 2;
        TreeNode root = new TreeNode(nodes[mid]);
        root.left = SortedListToBST(nodes, start, mid-1);
        root.right = SortedListToBST(nodes, mid+1, end);
        return root;
    }
}