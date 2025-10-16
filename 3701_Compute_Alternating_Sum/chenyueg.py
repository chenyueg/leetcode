class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_sum=0
        odd_sum=0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum -= nums[i]
        result = even_sum + odd_sum
        
        return result