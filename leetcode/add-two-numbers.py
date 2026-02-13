/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addHelper(l1, l2, false);
    }

    ListNode* addHelper(ListNode* l1, ListNode* l2, bool isCarryOut) {
        if (l1 == nullptr && l2 == nullptr) {
            if (isCarryOut) {
                return new ListNode(1);
            } 

            return nullptr;
        }

        int sum = 0; 

        if (l1 != nullptr) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != nullptr) {
            sum += l2->val;
            l2 = l2->next;
        }

        if (isCarryOut) sum += 1;

        bool newCarryOut = false;

        if (sum > 9) {
            newCarryOut = true;
            sum -= 10;
        }

        return new ListNode(sum, addHelper(l1, l2, newCarryOut));
    }
};