class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum([piles[::-1][i * 2 + 1] for i in range(len(piles) // 3)])
