class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        fin = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            fin += rem
            temp //= 10
        return fin if x % fin == 0 else -1