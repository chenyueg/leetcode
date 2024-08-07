class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        currentDepth = 0
        
        for char in s:
            if char == '(':
                currentDepth += 1
                maxDepth = max(maxDepth, currentDepth)
            elif char == ')':
                currentDepth -= 1
        
        return maxDepth