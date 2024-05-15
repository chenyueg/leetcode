class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        char_dict = {}
        result = 0
        for i in range(len(s)):
            c = s[i]
            char_dict[c] = i
        for j in range(len(t)):
            c = t[j]
            result += abs(char_dict[c] - j)
        return result
