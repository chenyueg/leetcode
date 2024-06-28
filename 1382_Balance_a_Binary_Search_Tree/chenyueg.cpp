/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> arr;
    TreeNode* balanceBST(TreeNode* root) 
    {
        inorder(root);
        return BST(0, arr.size()-1);
    }
    void inorder(TreeNode* root)
    {
        if (root != nullptr)
        {
            inorder(root->left);
            arr.push_back(root->val);
            inorder(root->right);
        }
    }
    TreeNode* BST(int l, int r)
    {
            if (l > r)
            {
                return nullptr;
            }
            int m = (l + r) / 2;
            auto left = BST(l, m - 1);
            auto right = BST(m + 1, r);
            return new TreeNode(arr[m], left, right);     

    }
};