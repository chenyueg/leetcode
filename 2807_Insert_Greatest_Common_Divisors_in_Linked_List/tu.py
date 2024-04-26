# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_common_div(self, num1, num2):
        result = 1
        div = 1
        for i in range(min(num1, num2)):
            if num1%div == 0 and num2%div == 0:
                result = div
            div += 1
        return result

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while(current.next != None):
            next = current.next
            new_node = ListNode(val=self.find_common_div(current.val, next.val), next=next)
            current.next = new_node
            current = next
        return head

        
