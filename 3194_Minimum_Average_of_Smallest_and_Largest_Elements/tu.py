class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        result = nums[0] + nums[-1]
        for i in range(len(nums) // 2):
            current = nums[i] + nums[-(i + 1)]
            result = min(result, current)
        return result / 2

