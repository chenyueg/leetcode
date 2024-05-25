class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        results = [0,0]
        pos = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            results[pos] += 10 ** (i // 2) * nums[i]
            pos = 1 - pos
        return results[0] + results[1]