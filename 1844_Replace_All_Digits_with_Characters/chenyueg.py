class Solution:
    def replaceDigits(self, s: str) -> str:
        new = ""
        
        for i in range(len(s)):
            if i % 2 == 0:
                new += s[i]
            else:
                new += chr(ord(s[i-1]) + int(s[i]))
        
        return new