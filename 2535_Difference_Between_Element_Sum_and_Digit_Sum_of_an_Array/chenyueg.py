class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eSum = sum(nums)
        dSum = 0
        for i in nums:
            for j in str(i):
                dSum += int(j)
        return eSum - dSum 