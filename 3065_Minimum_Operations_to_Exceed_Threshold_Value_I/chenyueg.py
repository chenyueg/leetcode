class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for each in nums:
            if each < k:
                count += 1
        return count