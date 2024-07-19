class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        all_sum = n * (n + 1) // 2
        right = n
        left = all_sum - n - (n - 1)
        for i in range(n - 2, 2, -1):
            if left == right:
                return i + 1
            left -= i
            right += i + 1
            if left < right:
                break
        return -1
