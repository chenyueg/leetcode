class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def char_to_int(char):
            return ord(char) - ord('a')
        sc = [0] * 26
        tc = [0] * 26
        for c in s:
            sc[char_to_int(c)] += 1
        for c in t:
            tc[char_to_int(c)] += 1
        result = 0
        for i in range(len(sc)):
            result += abs(sc[i] - tc[i])
        return result // 2
        