class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        l = len(arr)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if abs(arr[k] - arr[j]) <= b and abs(arr[k] - arr[i]) <= c and abs(arr[i] - arr[j]) <= a:
                        result += 1
        return result
        