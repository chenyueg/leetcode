class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for s in arr:
            if arr.count(s) == 1:
                k -= 1
            if k == 0:
                return s
        return ""
        