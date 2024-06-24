class Solution:
    def countDigits(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        count = 0
        for each in nums:
            if num % each == 0:
                count += 1
        return count