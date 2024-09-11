class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l = []
        
        for i in arr:
            arr.remove(i)
            if i not in arr:
                l.append(i)
            arr.insert(0,i)
        
        if k > len(l):
            return ""
        
        return l[k-1]