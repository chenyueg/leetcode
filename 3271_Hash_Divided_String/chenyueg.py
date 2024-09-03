class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ''
        n = len(s)

        for i in range(0, n, k):
            sub = s[i:i+k]
            temp = 0
            for char in sub:
                temp += (ord(char) - 97)
            new_char = chr((temp % 26) + 97)
            res += new_char
        
        return res