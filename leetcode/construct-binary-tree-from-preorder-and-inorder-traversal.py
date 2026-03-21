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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, inorder, 0, 0, inorder.size());
    }

    TreeNode* helper(const vector<int>& preorder, const vector<int>& inorder, const int leftPre, const int leftIn, const int rightIn) {
        if (leftIn >= rightIn) return nullptr;

        int index = leftIn;

        while (index < rightIn && inorder.at(index) != preorder.at(leftPre)) {
            ++index;
        }

        TreeNode* root = new TreeNode(preorder.at(leftPre));

        int leftSize = index - leftIn;

        root->left = helper(preorder, inorder, leftPre + 1, leftIn, index);

        root->right = helper(preorder, inorder, leftPre + 1 + leftSize, index + 1, rightIn);

        return root;       
    }
};