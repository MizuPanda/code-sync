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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int k = 0;

        for (ListNode* current = head; current != nullptr; current = current->next) {
            ++k;
        }

        k -= n;

        if (k == 0) return head->next;

        int i = 0;

        for (ListNode* current = head; current != nullptr; current = current->next) {
            if (i == k - 1) {
                current->next = current->next->next;
                break;
            }
            ++i;
        }

        return head;
    }
};