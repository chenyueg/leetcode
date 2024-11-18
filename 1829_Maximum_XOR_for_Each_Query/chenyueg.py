class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xorres = nums[0]
        max_xor = (1 << maximumBit) - 1
        ans = []
        
        for i in range(1, n):
            xorres ^= nums[i]
        
        for i in range(n):
            ans.append(xorres ^ max_xor)
            xorres ^= nums[n - 1 - i]
        
        return ans