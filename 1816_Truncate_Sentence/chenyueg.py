class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        if len(s) <= k:
            return " ".join(s)
        else:
            return " ".join(s[:k])