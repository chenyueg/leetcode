class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
         count = [b.count('1') for b in bank]
         new_count = [i for i in count if i != 0]
         final_count = [new_count[i]*new_count[i-1] for i in range(1, len(new_count))]
         return sum(final_count)