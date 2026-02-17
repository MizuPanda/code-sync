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
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;

        int longestPath = maxDepth(root->left) + maxDepth(root->right);

        return max({longestPath, diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)});
    }

    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        return max(maxDepth(root->left) + 1, maxDepth(root->right) + 1);
    }
};