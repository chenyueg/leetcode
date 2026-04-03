class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        result = 0
        for k, v in num_count.items():
            if v == 1:
                result = result + k
        return result    