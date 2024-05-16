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
    int result = 0;
public:
    int averageOfSubtree(TreeNode* root) {
        sumOfSubtree(root);
        return result;
    }

    std::tuple<int, int> sumOfSubtree(TreeNode* root)
    {
        if(!root)
        {
            return {0,0};
        }
        tuple<int, int> lefts = sumOfSubtree(root->left);
        int left_sum = get<0>(lefts);
        int left_count = get<1>(lefts);
        tuple<int, int> rights = sumOfSubtree(root->right);
        int right_sum = get<0>(rights);
        int right_count = get<1>(rights);
        int current_sum = root->val + left_sum + right_sum;
        int current_count = left_count + right_count + 1;
        if(current_sum / current_count == root->val)
        {
            result += 1;
        }
        return {current_sum, current_count};
    }
};