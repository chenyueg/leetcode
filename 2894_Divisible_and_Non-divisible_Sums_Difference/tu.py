class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_all = n * (n+1) // 2
        div_n = n // m
        sum_div = div_n * (m + m * div_n) // 2
        return sum_all - sum_div - sum_div
