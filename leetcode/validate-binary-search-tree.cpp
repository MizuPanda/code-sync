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

    bool isValidBST(TreeNode* root) {
        bool isFirst = true;
        int last;

        return dfs(root, last, isFirst);        
    }

    bool dfs(TreeNode* root, int& last, bool& isFirst) {
        if (!root) return true;

        if (!dfs(root->left, last, isFirst)) return false;

        if (isFirst) {
            last = root->val;
            isFirst = false;
        } else if (last < root->val) {
            last = root->val;
        } else {
            return false;
        }
        
        return dfs(root->right, last, isFirst);
    }
    // 2, 1, 3

};