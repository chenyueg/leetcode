class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            s = 0
            while num:
                tens = num % 10
                s += tens
                num //= 10
            res.append(s)
        return min(res)