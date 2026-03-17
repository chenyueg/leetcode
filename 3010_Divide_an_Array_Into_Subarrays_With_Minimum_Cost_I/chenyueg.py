class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        for i in range(1, 3):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums[0] + nums[1] + nums[2]