class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i %  2 == 0:
                count |= i
        return count