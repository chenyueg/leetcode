class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return len(words)-len({*map(frozenset,words)})
        