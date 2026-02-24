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
    int kthSmallest(TreeNode* root, int k) {
        int answer;
        int index = 0;
        dfs(root, k, index, answer);
        return answer;
    }

    void dfs(TreeNode* root, const int k, int& index, int& answer) {
        if (!root || index == k) return ;

        dfs(root->left, k, index, answer);

        ++index;

        if (index == k) {
            answer = root->val;
            return ;
        }

        dfs(root->right, k, index, answer);

    }
};