class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        previous = 0
        result = [0] * len(nums)
        for i in range(len(nums)):
            left += previous
            right -= nums[i]
            previous = nums[i]
            result[i] = abs(left - right)
        return result
