class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = 0
        m, p, g = False, False, False
        
        for each in garbage:
            time += len(each)
        for i in range(len(travel), 0, -1):
            m = m or 'M' in garbage[i]
            p = p or 'P' in garbage[i]
            g = g or 'G' in garbage[i]
            time += travel[i-1] * (m + p + g)
        return time