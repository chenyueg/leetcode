class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        bits = 0
        
        for num in nums:
            q, r = divmod(num, original)
            if r == 0 and (q & (q - 1)) == 0:
                bits |= q
       
        n = bits + 1
       
        return original * (n & -n)