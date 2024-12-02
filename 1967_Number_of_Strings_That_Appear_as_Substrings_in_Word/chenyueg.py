class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(count in word for count in patterns)