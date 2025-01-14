class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for each in words:
            if each.startswith(pref):
                count += 1
        return count