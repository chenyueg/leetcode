class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cs = Counter(nums)
        num2s = [y for y,count in cs.items() if count == 2]
        result = 0
        for num in num2s:
            result ^= num
        return result     
