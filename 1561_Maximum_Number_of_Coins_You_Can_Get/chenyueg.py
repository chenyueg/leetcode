class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        pair = len(piles) // 3
        for i in range(pair, len(piles), 2):
            coins += piles[i]
        return coins