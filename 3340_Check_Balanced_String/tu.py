class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = sum([int(num[i]) for i in range(len(num)) if i % 2 == 0])
        odd_sum = sum([int(num[i]) for i in range(len(num)) if i % 2 == 1])
        return even_sum == odd_sum