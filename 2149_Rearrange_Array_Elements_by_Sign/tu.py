class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
