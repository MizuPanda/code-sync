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
    bool isBalanced(TreeNode* root) {
        if (!root) return true;

        bool balanced = abs(maxDepth(root->left) - maxDepth(root->right)) < 2;

        return balanced && isBalanced(root->left) && isBalanced(root->right);
    }

    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        return max(maxDepth(root->left) + 1, maxDepth(root->right) + 1);
    }
};