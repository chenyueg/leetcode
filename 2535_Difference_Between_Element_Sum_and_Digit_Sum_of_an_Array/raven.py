class Solution:
  def differenceOfSum(self, nums: List[int]) -> int:
    sum = 0
    dsum = 0
    for i in nums:
      sum += i
      while i > 0:
        dsum += i % 10
        i = i // 10
    
    return sum - dsum
       
