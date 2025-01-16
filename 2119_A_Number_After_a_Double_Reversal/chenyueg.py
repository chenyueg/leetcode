class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or not str(num).endswith("0")