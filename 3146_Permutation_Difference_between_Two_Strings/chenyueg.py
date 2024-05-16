class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sDict = {}
        tDict = {}
        
        for i in range(len(s)):
            sDict[s[i]] = i
            tDict[t[i]] = i

        count = 0
        
        for char, index in sDict.items():
            count += abs(index - tDict[char])
        
        return count