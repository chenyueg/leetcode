class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = []
        for i in range(len(nums)):
            new_add = []
            for j in range(len(result)):
                new_add.append(result[j] ^ nums[i])
            result.append(nums[i])
            result.extend(new_add)

        return sum(result)
