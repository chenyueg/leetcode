class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        curr = ''
        
        for i in target:
            curr += 'a'
            ans.append(curr)
            
            while curr[-1] != i:
                curr = curr[:-1] + chr((ord(curr[-1]) + 1))
                ans.append(curr)
        
        return ans