class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [p[0] for p in points]
        xs.sort()
        max_width = 0
        for i in range(1,len(xs)):
            max_width = max(max_width, xs[i]-xs[i-1])
        return max_width