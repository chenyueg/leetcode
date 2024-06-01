# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head;
        next = current.next
        while (next):
            if next.val != 0:
                current.val += next.val
            else:
                if next.next:
                    current.next = next
                    current = next
                else:
                    current.next = None
            next = next.next
        return head
