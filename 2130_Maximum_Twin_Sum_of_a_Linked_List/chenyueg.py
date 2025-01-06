# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        k = []
        max_sum = 0
        
        while(head.next != None):
            
            k.append(head.val)
            head = head.next
            
            if(head.next == None):
                k.append(head.val)
        
        for i in range(len(k) // 2):
            
            sum = k[i] + k[len(k)-1-i]
            
            if(sum>max_sum):
                max_sum = sum
        
        return max_sum