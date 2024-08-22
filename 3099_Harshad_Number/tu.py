class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        x_sum = 0
        while temp > 0:
            x_sum += temp % 10
            temp = temp // 10
        if x % x_sum == 0:
            return x_sum
        else:
            return -1