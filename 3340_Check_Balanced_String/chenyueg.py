class Solution:
    def isBalanced(self, num: str) -> bool:
        array = [int(i) for i in str(num)]
        return sum(array[::2]) == sum(array[1::2])