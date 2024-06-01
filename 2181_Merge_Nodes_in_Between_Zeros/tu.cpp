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
    ListNode* mergeNodes(ListNode* head) {
        head;
        ListNode* current = head;
        ListNode* next = current->next;
        while(next)
        {
            if(next->val != 0)
            {
                current->val += next->val;
            }
            else
            {
                if(next->next)
                {
                    current->next = next;
                    current = next;
                }
                else
                {
                    current->next = nullptr;
                }
            }
            next = next->next;
        }
        current = nullptr;
        return head;
    }
};