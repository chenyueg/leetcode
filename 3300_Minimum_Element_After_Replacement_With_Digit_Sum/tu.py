class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = 99999999
        for num in nums:
            _sum = 0
            while num > 0:
                _sum += num % 10
                num //= 10
            result = min(result, _sum)
        return result
