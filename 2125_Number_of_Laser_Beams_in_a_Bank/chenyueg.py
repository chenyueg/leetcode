class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prevRow = 0
        for eachRow in bank:
            row = eachRow.count("1")
            if row:
                total += prevRow * row
                prevRow = row
        return total