class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        u_nums = counts.keys()

        result = 0
        for num in u_nums:
            if num + k in counts:
                result += counts[num] * counts[num + k]
        return result
