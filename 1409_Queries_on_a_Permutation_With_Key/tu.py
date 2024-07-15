class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        temp = [i + 1 for i in range(m)]

        for q in queries:
            result.append(temp.index(q))
            temp.remove(q)
            temp.insert(0, q)

        return result
