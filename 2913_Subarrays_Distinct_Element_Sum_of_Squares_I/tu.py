class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums) + 1):
            for j in range(len(nums) - i + 1):
                result += len(set(nums[j:j+i])) ** 2
        return result
        