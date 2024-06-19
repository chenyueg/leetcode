class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newS=[None] * len(s)
        for i in range(len(indices)):
            newS[indices[i]] = s[i]
        return "".join(newS)