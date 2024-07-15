class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        for num in nums:
            if num + diff in nums and num + diff * 2 in nums:
                result += 1
        return result
