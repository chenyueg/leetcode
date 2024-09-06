class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        arr = list(s)
        left = 0
        right = len(arr) - 1
        ops = 0
        
        while left < right:
            if arr[left] != arr[right]:
                if arr[left] > arr[right]:
                    arr[left] = arr[right]
                else:
                    arr[right] = arr[left]
            ops += 1
            left += 1
            right -= 1

        if ops == 0:
            return s

        result = ""
        
        for i in arr:
            result += i

        return result