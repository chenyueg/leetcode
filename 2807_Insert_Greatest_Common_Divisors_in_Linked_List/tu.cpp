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
    int findCommonDivisor(int num1, int num2){
        int result = 1;
        int div = 1;
        int min_num = min(num1, num2);
        while(div<=min_num){
            if(num1%div == 0 && num2%div == 0)
            {
                result = div;
            }
            div++;
        }
        return result;
    }

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* current = head;
        while(current->next!=nullptr)
        {
            ListNode* next = current->next;
            int new_value = findCommonDivisor(current->val, next->val);
            ListNode* new_node = new ListNode(new_value, next);
            current->next = new_node;
            current = next;
        }
        return head;
    }
};
