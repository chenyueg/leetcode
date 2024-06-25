class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        result = 0
        while temp > 0:
            current = temp % 10
            if num % current == 0:
                result += 1
            temp //= 10
        return result
