class Solution:
#  def countKDifference(self, nums: List[int], k: int) -> int:
#    count = 0
#    n = len(nums)
#    for i in range(n - 1):
#      for j in range(i + 1, n):
#        if abs(nums[i] - nums[j]) == k:
#          count += 1
#    
#    return count

        
  def countKDifference(self, nums: List[int], k: int) -> int:
    d = collections.defaultdict(int)
    for i in nums:
      d[i] += 1
    
    count = 0
    keys = d.keys()
    for i in keys:
      if i + k in keys:
        count += d[i] * d[i + k]
    
    return count
     
