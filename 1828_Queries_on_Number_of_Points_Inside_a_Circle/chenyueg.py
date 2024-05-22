class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        count = 0
        for query in queries:
            x1 = query[0]
            y1 = query[1]
            r = query[2]
            for point in points:
                x2 = point[0]
                y2 = point[1]
                if (((x2 - x1) ** 2 + (y2 - y1) ** 2)) <= r * r:
                    count = count + 1
            res.append(count)
            count = 0
        return res