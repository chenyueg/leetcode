class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out = k
        for i in range(0, len(nums)):
            out ^= nums[i]
        return out.bit_count()
