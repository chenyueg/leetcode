class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0
        for each in gain:
            current += each
            highest = max(current, highest)
        return highest