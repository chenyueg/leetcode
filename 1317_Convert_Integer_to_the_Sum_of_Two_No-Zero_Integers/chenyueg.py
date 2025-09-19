class Solution:
    def check(self, x):
        return '0' not in str(x)
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            j = n - i
            if self.check(i) and self.check(j):
                return [i, j]