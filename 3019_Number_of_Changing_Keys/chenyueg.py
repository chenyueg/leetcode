class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        
        for a, b in zip(s, s[1:]):
            if a.lower() != b.lower():
                changes += 1  
        
        return changes