class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        totalSum = 0

        for i, num in enumerate(nums):
            totalSum += sum(nums[max(0, i-num):i+1])

        return totalSum