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
    int goodNodes(TreeNode* root) {
        return helper(root, root->val);
    }

    int helper(TreeNode* root, int maxVal) {
        if (!root) return 0;

        const int good = root->val >= maxVal? 1 : 0;

        maxVal = max(root->val, maxVal);

        return good + helper(root->left, maxVal) + helper(root->right, maxVal);
    }
};