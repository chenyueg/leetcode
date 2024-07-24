class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for ch in s:
            if ch != 'i':
                res += ch
            if ch == 'i':
                res = res[::-1]
        return res