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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        helper(root, res, 0);

        return res;
    }

    void helper(TreeNode* root, vector<vector<int>>& v, int level) {
        if (!root) return ;

        if (v.size() <= level) {
            v.push_back({});
        }

        v.at(level).emplace_back(root->val);

        helper(root->left, v, level + 1);
        helper(root->right, v, level + 1);
    }
};