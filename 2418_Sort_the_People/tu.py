class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined_list = [[heights[i], names[i]] for i in range(len(names))]
        combined_list.sort(reverse=True)
        result = [k for v, k in combined_list]
        return result

