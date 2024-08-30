class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        flag = True
        
        for char in s:
            if flag and char == '*':
                count += 1
            if char == '|':
                flag = not flag
        
        return count