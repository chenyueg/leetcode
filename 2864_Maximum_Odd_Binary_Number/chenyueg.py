class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')

        if ones == 1:
            return "0" * (n - 1) + '1'
        elif ones > 1:
            return '1' * (ones - 1) + '0' * (n - ones) + '1'
        else:
            return '0' * n