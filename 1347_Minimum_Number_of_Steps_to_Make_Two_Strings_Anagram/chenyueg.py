class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        x = list(s)
        x = set(x)
        
        for i in x:
            
            p = s.count(i)
            q = t.count(i)
            
            if q >= p:
                continue
            else:
                ans += p
                ans -= q
        
        return ans