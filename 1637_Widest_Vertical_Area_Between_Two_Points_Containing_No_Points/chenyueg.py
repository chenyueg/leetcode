class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        hor = []
        for i in range(len(points)):
            hor.append(points[i][0])
        hor.sort()
        diff = 0
        for j in range(len(hor)-1):
            if hor[j+1] - hor[j] > diff:
                diff = hor[j+1] - hor[j]
            else:
                continue
        return diff