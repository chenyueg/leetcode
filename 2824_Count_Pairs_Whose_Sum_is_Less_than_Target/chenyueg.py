class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = 0
        low = 0
        high = len(nums)-1
        while low < high:
            if nums[low] + nums[high] < target:
                sum += high - low
                low += 1
            else:
                high -= 1
        return sum