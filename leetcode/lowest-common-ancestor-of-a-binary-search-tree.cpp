/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // init pStack and qStack
        // pop top()
        // if topP == topQ, res = topP
        TreeNode* res;
        
        stack<pair<TreeNode*, int>> pStack;
        stack<pair<TreeNode*, int>> qStack;

        TreeNode* currentP = root;
        TreeNode* currentQ = root;

        while (currentP != nullptr || currentQ != nullptr) {
            if (currentP) {
                pStack.push({currentP, pStack.size()});

                if (currentP->val > p->val) {
                    currentP = currentP->left;
                } else if (currentP->val < p->val) {
                    currentP = currentP->right;
                } else {
                    currentP = nullptr;
                }
            }

            if (currentQ) {
                qStack.push({currentQ, qStack.size()});

                if (currentQ->val > q->val) {
                    currentQ = currentQ->left;
                } else if (currentQ->val < q->val) {
                    currentQ = currentQ->right;
                } else {
                    currentQ = nullptr;
                }
            }
        }

        while (!pStack.empty() && !qStack.empty()) {
            if (pStack.top().first->val == qStack.top().first->val) {
                res = pStack.top().first;
                break;
            } else if (pStack.top().second < qStack.top().second) {
                qStack.pop();
            } else {
                pStack.pop();
            }
        }

        return res;
    }
};