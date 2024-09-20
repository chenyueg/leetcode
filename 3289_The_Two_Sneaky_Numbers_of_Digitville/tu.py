class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [n for n, count in Counter(nums).items() if count > 1]
        