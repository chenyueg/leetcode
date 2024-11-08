class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: chr, x: int) -> chr:
            # Handle lowercase letters
            if 'a' <= c <= 'z':
                base = ord('a')
                shifted = (ord(c) - base + x) % 26 + base
                return chr(shifted)
            
            # Handle uppercase letters
            elif 'A' <= c <= 'Z':
                base = ord('A')
                shifted = (ord(c) - base + x) % 26 + base
                return chr(shifted)
            
            # Non-alphabetical characters are returned unchanged
            else:
                return c
        
        s_list = [c for c in s]
        for i in range(len(s_list)):
            if '0' <= s_list[i] <= '9':
                s_list[i] = shift(s_list[i-1], int(s_list[i])) 
        return ''.join(s_list)