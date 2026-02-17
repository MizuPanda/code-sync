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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) {
            return isSameTree(root, subRoot);
        }

        bool isSub = false;

        if (root->val == subRoot->val) {
            isSub = isSameTree(root, subRoot);
        }
        if (!isSub) {
            isSub = isSubtree(root->left, subRoot); 
            isSub = isSub || isSubtree(root->right, subRoot);
        }

        return isSub;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p || !q) return p == q;

        if (p->val != q->val || !isSameTree(p->left, q->left) || !isSameTree(p->right, q->right)) {
            return false;
        }

        return true;
    }
};