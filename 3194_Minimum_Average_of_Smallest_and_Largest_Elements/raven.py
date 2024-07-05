class Solution:
  def minimumAverage(self, nums: List[int]) -> float:
    n = len(nums)
    nums.sort()
    
    ret = float('inf')
    for i in range(n // 2):
      avg = (nums[i] + nums[n - 1 - i]) / 2
      ret = min(ret, avg)
    
    return ret   
      
