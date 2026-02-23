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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> v;

        helper(v, root, 0);

        return v;
    }

    void helper(vector<int>& v, TreeNode* root, int level) {
        if (!root) return;

        if (level == v.size()) {
            v.push_back(root->val);
        }

        helper(v, root->right, level + 1);
        helper(v, root->left, level + 1);
    }
};